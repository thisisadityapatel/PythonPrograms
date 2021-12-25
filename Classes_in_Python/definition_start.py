#creating a basic class
class Books:
    def __init__(self, title):
        self.title = title

b1 = Books("Life is what you make it")
b2 = Books("Crazy times with uncle ken")

print(b1)
print(type(b1))
print(b1.title)
