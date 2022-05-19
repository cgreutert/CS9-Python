# BookCollection
from Book import Book
from BookCollectionNode import BookCollectionNode
class BookCollection:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count
    def insertBook(self, book):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() > book:
                found = True
            else:
                previous = current
                current = current.getNext()
        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    def getBooksByAuthor(self, author):
        current = self.head
        output = ""
        while current != None:
            if current.getData().getAuthor().upper() == author.upper():
                output += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return output
    def getAllBooksInCollection(self):
        current = self.head
        output = ""
        while current != None:
            output += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return output

