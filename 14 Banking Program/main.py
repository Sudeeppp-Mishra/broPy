balance = 0

def show_balance():
    print(f"\nYour balance is ${balance:.2f}\n")

def deposit(depositAmt):
    global balance
    
    if depositAmt < 0:
        print("\nThat's not a valid amount!\n")
    else:
        balance+=depositAmt
        print(f"\n${depositAmt:.2f} deposited successfully!\n")
    

def withdraw(withdrawAmt):
    global balance
    
    if balance<withdrawAmt:
        print("\nInsufficient Balance!\n")
    elif withdrawAmt<0:
        print("\nAmount must be greater than 0!\n")
    else:
        balance-=withdrawAmt
        print(f"\n${withdrawAmt:.2f} withdrawn successfully!\n")

def main():
    is_running = True

    while is_running:
        print("-----BANKING PROGRAM-----")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4):")
        
        if choice == '1':
            show_balance()
            
        elif choice == '2':
            depositAmt = float(input("Enter amount to be deposited: "))
            deposit(depositAmt)
            
        elif choice == '3':
            withdrawAmt = float(input("Enter amount to be withdrawn: "))
            withdraw(withdrawAmt)
            
        elif choice == '4':
            is_running = False
            
        else:
            print("That is not a valid choice!")
            
    print("\nThank you! Have a nice day!\n")
    

if __name__ == '__main__':
    main()