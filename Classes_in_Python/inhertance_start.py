#starting with inheritance

class Publications:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publications):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

class Books(Publications):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazines(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

class Newspapers(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Books("Life is what you make it", "Peter Buffet", 120, 100)
n1 = Newspapers("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazines("Scientific America", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)

        
