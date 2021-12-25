#Type Check Start

class Books():
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    
    #using the class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    def set_title(self, newtitle):
        self.title = newtitle
    
    #using the instance methods
    def __init__(self, title, booktype):
        self.title = title
        if not booktype.upper() in Books.BOOK_TYPES:
            raise ValueError(f"{booktype.upper()} not a valid booktype")
        else:
            self.booktype = booktype.upper()

#acccess the class attribute
print(Books.getbooktypes())

#making insatnces of the class
b1 = Books("Title 1", "Hardcover")
b2 = Books("Title 2", "Paperback")



