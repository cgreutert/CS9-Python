# Book.py
class Book:
    def __init__(self, title="", author="", year=None):
        self.title = str(title)
        self.author = str(author)
        self.year = year
        if self.year != None:
            self.year = int(year)
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getYear(self):
        return self.year
    def getBookDetails(self):
        return "Title: {}, Author: {}, Year: {}".format(self.title, self.author, self.year)
    def __gt__(self, rhs):
        if (self.author.upper() == rhs.author.upper()) and (self.year == rhs.year):
            return self.title > rhs.title
        elif (self.author.upper() == rhs.author.upper()):
            return self.year > rhs.year
        else:
            return self.author.upper() > rhs.author.upper()

