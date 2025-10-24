def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sptrinkles ;)*")
        func(*args, **kwargs) 
    return wrapper
  
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge :3*")
        func(*args, **kwargs)
    return wrapper
        
@add_fudge
@add_sprinkles  
def get_ice_cream(flavor): # if the main function takes argument we need to set up wrapper function to take arguments as well so for any no. of arguments or keyword arguments
    print(f"Here is your {flavor} ice cream :)")
   
get_ice_cream("vanilla")