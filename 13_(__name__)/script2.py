from script1 import *

def fav_drink(drink):
    print(f"Your fav. drink is {drink}")
 
def main():   
    print("This is script2")
    fav_food("Sushi")
    fav_drink("Red Bull")
    print("goodbye!")

if __name__ == '__main__':
    main()