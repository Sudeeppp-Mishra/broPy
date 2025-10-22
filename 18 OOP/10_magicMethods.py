# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self): # By default if we pring book1 object it will return a memory address but this magic method can customize what to return when we print an object
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages<other.num_pages
    
    def __gt__(self, other):
        return self.num_pages>other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages+other.num_pages} pages"
    
    def __contains__(self, keyword): # keyword is what we are searching for
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' not found!"

        
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 280)


print(book1)
print(book2)
print(book3)

print(book1 == book4) # by default even if we have same author and title in two book objects it will return False cuz they are two different objects right but with the help of __eq__ (equal) dunder method we can customize that

print(book2 < book3) # it will be an error cuz we can't use this operator between instances but we can customize using __lt__ (less than) 
# we can use __gt__() for greater than

print(book4>book3)

print(book2+book3) # + is also not supported but we can customize it with __add__ method

print("Lion" in book3) # it is also not legal so we can customize using __contains__()
print("Rowling" in book2)
print("Rowling" in book3)

print(book1['title']) # it's also err to customize we use __getitem__()
print(book3['author'])
print(book4['num_pages'])
print(book1['audio'])
    