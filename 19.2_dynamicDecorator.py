def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles ;)*")
        return func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge :3*")
        return func(*args, **kwargs)
    return wrapper

def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream :)")

# --- Calls with different toppings ---

# Both fudge and sprinkles
decorated = add_fudge(add_sprinkles(get_ice_cream))
decorated("vanilla")

print("---")

# Only sprinkles
decorated = add_sprinkles(get_ice_cream)
decorated("chocolate")

print("---")

# No toppings
get_ice_cream("strawberry")

"""
Python Decorators: Flexible Behavior Example

Decorators are functions that wrap another function to extend or modify its behavior
without changing the original function.

Example: Ice Cream Toppings

def add_sprinkles(func):
    # Wrapper function allows any arguments (*args, **kwargs)
    # Adds sprinkles behavior before calling the original function
    ...

def add_fudge(func):
    # Wrapper function allows any arguments
    # Adds fudge behavior before calling the original function
    ...

def get_ice_cream(flavor):
    # Main function prints the ice cream flavor
    ...

Key Points:
1. Wrapper function:
   - Accepts *args and **kwargs to support any function signature.
   - Executes additional actions before or after the original function.

2. Multiple decorators:
   - Can stack decorators to combine behaviors.
   - Example: add both fudge and sprinkles
       decorated = add_fudge(add_sprinkles(get_ice_cream))
       decorated("vanilla")
       Output:
         *You add fudge :3*
         *You add sprinkles ;)*
         Here is your vanilla ice cream :)

3. Flexible usage:
   - Only one decorator:
       decorated = add_sprinkles(get_ice_cream)
       decorated("chocolate")
       Output:
         *You add sprinkles ;)*
         Here is your chocolate ice cream :)

   - No decorator:
       get_ice_cream("strawberry")
       Output:
         Here is your strawberry ice cream :)

Advantages:
- Reusable behavior: apply the same decorator to multiple functions
- Flexible combinations: choose which decorators to apply
- Keeps original function intact

Tip:
You can use the @decorator syntax:
@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    ...
This is equivalent to manual wrapping: add_fudge(add_sprinkles(get_ice_cream))
"""