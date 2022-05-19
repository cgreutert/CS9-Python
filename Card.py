# Card.py
class Card:
    def __init__(self, suit, rank):
        self.suit = str(suit)
        self.rank = str(rank)
        self.count = 1
        self.left = None
        self.right = None
        self.parent = None

    def getSuit(self):
        return self.suit
    def setSuit(self, suit):
        self.suit = str(suit)
    def getRank(self):
        return self.rank
    def setRank(self, rank):
        self.rank = str(rank)
    def getCount(self):
        return self.count
    def setCount(self, count):
        self.count = int(count)
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent
    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left
    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right
    def is_root(self):
        return not self.parent
    def isLeaf(self):
        return not (self.right or self.left)
    def has_left_child(self):
        return self.left
    def has_right_child(self):
        return self.right
    def is_left_child(self):
        return self.parent and str(self.parent.left) == str(self)
    def is_right_child(self):
        return self.parent and str(self.parent.right) == str(self)
    def has_any_children(self):
        return self.right or self.left
    def has_both_children(self):
        return self.right and self.left

    def replace_node_data(self, suit, rank, lc, rc):
        self.suit = suit
        self.rank = rank
        self.left = lc
        self.right = rc
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self
    def splice_out(self):
        if self.isLeaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def __str__(self):
        return "{} {} | {}\n".format(self.suit.upper(), self.rank.upper(), self.count)
    def __gt__(self, rhs):
        if self.rank.upper() == rhs.rank.upper():
            return self.suit.upper() > rhs.suit.upper()
        else:
            ranks = {"A": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,\
                     "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
            return ranks.get(self.rank.upper()) > ranks.get(rhs.rank.upper())
    def __lt__(self, rhs):
        if self.rank.upper() == rhs.rank.upper():
            return self.suit.upper() < rhs.suit.upper()
        else:
            ranks = {"A": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,\
                     "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
            return ranks.get(self.rank.upper()) < ranks.get(rhs.rank.upper())
    def __eq__(self, rhs):
        return self.rank.upper() == rhs.rank.upper() and self.suit.upper() == rhs.suit.upper()
