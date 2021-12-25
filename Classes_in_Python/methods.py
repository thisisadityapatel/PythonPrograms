#using different types of methods in python
# 1. Instance methods
# 2. Class methods
# 3. Static methods

class Books:
    BOOK_TYPE = ("PAPERBACK", "HARDCOVER", "EBOOK")

    #creating a class method to return the BOOK_TYPE attribute
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPE

    #creating a static method to make a list of all the books that are being created
    __booklist = None


    def __init__(self, title, booktype):
        self.title = title
        if booktype.upper() not in Books.BOOK_TYPE:
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype
    

    def set_title (self, title):
        self.title = title
    
    @staticmethod
    def getbooklist():
        if Books.__booklist == None:
            Books.__booklist = []
        return Books.__booklist


b1 = Books("Life is what you make it", "Paperback")
b2 = Books("Crazy time with uncle Ken", "Hardcover")

books = Books.getbooklist()
books.append(b1)
books.append(b2)

print(books)



    


