# Decorator = A function that extends the behavior of anotehr function
#             without (w/o) modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

# def add_sprinkles(func):
#     def wrapper(): # it is necessary to have this wrapper function
#         print("*You add sptrinkles ;)*")
#         func() # it's just like print("Here is your ice cream :)") so we are just decorating by "You add sprinkles"
#     return wrapper
  
# @add_sprinkles  
# def get_ice_cream():
#     print("Here is your ice cream :)")
    
# get_ice_cream()


# WHAT IF WE DON'T ADD WRAPPER FUNCTION

def add_sprinkles(func):
    print("*You add sptrinkles ;)*")
    func() 
  
@add_sprinkles  
def get_ice_cream():
    print("Here is your ice cream :)")
    
# here even if we haven't called get_ice_cream() funciton after we add the decorator @add_sprinkles it's automatically being called so not to do so we need wrapper function