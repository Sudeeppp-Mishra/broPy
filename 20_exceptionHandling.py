# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#              1. try,  2. except,  3. finally

# try:
#     # Try some code
# except Exception:
#     # Handle an Exception
# finally:
#     # Do some clean up

try:
    number = int(input("Enter a number: "))
    print(1/number)
# except Exception: # It can catch all exceptions but it's considered bad practice (Too broad exception clause)
#     print("Something went wrong!")
    
except ZeroDivisionError:
    print("You can't divide by 0 IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")

