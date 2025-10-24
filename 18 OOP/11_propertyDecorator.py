# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width # the first _ means they are private and they shouldn't be accessed outside of the class directly it just tells that (protected but we can technically)
        self._height = height
       
    @property 
    def width(self):
        return f"{self._width:.2f} cm"
    
    @property
    def height(self):
        return f"{self._height:.2f} cm"
    
    # NOTE: Getter methods with @property
    # --------------------------------------
    # - The @property decorator lets us define a method that acts like an attribute.
    # - This helps us customize *how* an attribute’s value is returned (read access).
    # - Example use cases:
    #     - Formatting output (e.g., showing "cm" or rounding values)
    #     - Validating or transforming data before returning it
    #     - Making internal/private attributes (_width, _height) read-only from outside
    #
    # So instead of accessing raw data like `self._width`,
    # we can use a getter property that returns a processed or formatted version:
    #
    #     @property
    #     def width(self):
    #         return f"{self._width:.2f} cm"
    #
    # Access: rectangle.width  ← acts like an attribute, not a method call

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height= new_height
        else:
            print("Height must be greater than 0")
            
    # NOTE: Setter methods with @<property>.setter
    # --------------------------------------------
    # - The setter lets us define how an attribute’s value is updated (write access).
    # - It allows us to add validation, transformation, or restrictions when setting values.
    # - Example use cases:
    #     - Preventing invalid data (e.g., negative width or height)
    #     - Automatically converting or formatting input
    #     - Logging or tracking changes to attributes
    #
    # Example:
    #     @width.setter
    #     def width(self, new_width):
    #         if new_width > 0:
    #             self._width = new_width
    #         else:
    #             print("Width must be greater than 0")
    #
    # Access:
    #     rectangle.width = 5  ← behaves like setting an attribute, but actually runs logic
            
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
        
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
        
    # NOTE: Deleter methods with @<property>.deleter
    # ----------------------------------------------
    # - The deleter allows us to define custom behavior when deleting an attribute.
    # - It’s useful when we want to clean up resources, enforce restrictions,
    #   or simply print/log a message when an attribute is deleted.
    # - Example use cases:
    #     - Automatically releasing memory or resources
    #     - Preventing deletion of critical attributes
    #     - Logging attribute deletions
    #
    # Example:
    #     @width.deleter
    #     def width(self):
    #         del self._width
    #         print("Width has been deleted")
    #
    # Access:
    #     del rectangle.width  ← deletes attribute and triggers custom logic

        
rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = -1

print(rectangle.width) # now if we access these width and height it will return whatever is inside the property decorators of width() and height() methods
print(rectangle.height)

del rectangle.width # to delete we use this del keyword
del rectangle.height

# NOTE: Relationship Between @property, @setter, and @deleter
# ------------------------------------------------------------
# - You CANNOT use @<property>.setter or @<property>.deleter 
#   without first defining a @property for that same attribute.
#
# WHY?
# - Because the setter and deleter are *linked* to an existing property name.
#   They don’t work independently — they modify the behavior of the property itself.
#
# Example ❌ (Invalid):
#     @width.setter
#     def width(self, new_width):
#         self._width = new_width
#   → Error: 'width' property doesn’t exist yet.
#
# Example ✅ (Correct order):
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, new_width):
#         self._width = new_width
#
# So: Always define the @property (getter) first → then add @setter or @deleter.

# ---------------------------------------------------------
# NOTE: Public, Protected, and Private Attributes in Python
# ---------------------------------------------------------
# - Python does not strictly enforce access levels; it uses naming conventions.
#
#   1️⃣ Public: self.name
#       → Freely accessible everywhere.
#
#   2️⃣ Protected: self._name
#       → Meant for internal use; still accessible outside, but not recommended.
#
#   3️⃣ Private: self.__name
#       → Name-mangled to _ClassName__name to avoid accidental access.
#
# - In @property usage:
#       Use a single underscore (self._name) for the actual data,
#       and expose it via a property (def name(self):) for controlled access.
#
#       Example:
#           self._name = "Sudeep"
#           @property def name(self): return self._name


#<<-------------------------------------------------------------->>
# ---------------- Python Attribute Access Levels ----------------
# In Python, access levels are based on naming conventions rather than strict enforcement.
# Python trusts programmers to use attributes responsibly ("we're all adults here" philosophy).

# 1. Public Attribute
#   - No leading underscores
#   - Can be accessed and modified freely
#   Example: self.name
#   Access: obj.name

# 2. Protected Attribute
#   - Single leading underscore _
#   - Intended for internal use by class and subclasses
#   - Can be accessed externally but should be treated as "internal"
#   Example: self._name
#   Access: obj._name  (technically works, but not recommended)

# 3. Private Attribute (Name Mangling)
#   - Double leading underscore __
#   - Not directly accessible outside the class
#   - Internally, Python changes the name to _ClassName__attribute
#   Example: self.__name
#   Access: obj._ClassName__name (technically possible, but discouraged)

# Summary:
# - Python does not enforce strict access control; conventions communicate intent.
# - Leading underscore(s) signal "internal use" or "private" to other programmers.
# - Use these conventions to protect internal state but Python allows access if needed.