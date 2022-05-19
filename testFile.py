# testFile.py
from Card import Card
from PlayerHand import PlayerHand
import pytest

def test_Cardgt():
    c1 = Card("c", "A")
    c2 = Card("D", "2")
    c3 = Card("H", "A")
    c4 = Card("h", "10")
    assert (c1 > c2) == False
    assert (c2 > c1) == True
    assert (c2 > c3) == True
    assert (c3 > c4) == False
    assert (c1 > c3) == False
    assert (c3 > c1) == True
def test_Cardlt():
    c1 = Card("c", "A")
    c2 = Card("D", "2")
    c3 = Card("H", "A")
    c4 = Card("h", "10")
    assert (c1 < c2) == True
    assert (c2 < c1) == False
    assert (c2 < c3) == False
    assert (c3 < c4) == True
    assert (c4 < c1) == False
    assert (c1 < c3) == True
    assert (c3 < c1) == False
def test_Cardeq():
    c1 = Card("c", "A")
    c2 = Card("C", "a")
    c3 = Card("C", "1")
    c4 = Card("h", "10")
    c5 = Card("H", "J")
    c6 = Card("h", "j")
    assert (c1 == c2) == True
    assert (c2 == c3) == False
    assert (c2 == c4) == False
    assert (c4 == c5) == False
    assert (c5 == c6) == True

def test_constructhand():
    hand = PlayerHand()
    assert hand.root == None
    assert hand.size == 0
    assert hand.isEmpty() == True

def test_put():
    hand = PlayerHand()
    hand.put('D', 'A')
    assert hand.root.suit == "D"
    assert hand.root.rank == "A"
    assert hand.root.has_left_child() == None
    assert hand.root.has_right_child() == None
    assert hand.root.is_left_child() == None
    assert hand.root.is_right_child() == None
    assert hand.root.has_any_children() == None
    assert hand.root.has_any_children() == None
    assert hand.root.isLeaf() == True
    assert hand.root.has_both_children() == None
    assert hand.isEmpty() == False
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.inOrder() == \
"D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"
    assert hand.preOrder() == \
"D A | 1\n\
S K | 2\n\
S 2 | 1\n\
C Q | 1\n\
H 7 | 1\n\
C K | 1\n"
    hand.root.replace_node_data("H", "A", None, None)
    assert hand.root.suit == "H"
    assert hand.root.rank == "A"
    assert hand.preOrder() == "H A | 1\n"

def test_get():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.get("S", "K") == Card("S", "K")
    assert hand.get("C", "Q") == Card("C", "Q")
    assert hand.get("H", "7") == Card("H", "7")
    assert hand.get("S", "3") == None
    assert hand.get("H", "K") == None

def test_getMin():
    hand = PlayerHand()
    hand.put('D', 'A')
    assert hand.getMin() == Card("D", "A")
    hand.put('S', 'A')
    assert hand.getMin() == Card("D", "A")
    hand.put('C', '1')
    assert hand.getMin() == Card("D", "A")
    hand.put('C', 'A')
    assert hand.getMin() == Card("C", "A")

def test_getSuccessor():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.getSuccessor('D', 'A') == None
    hand.getSuccessor('S', 'K') == None
    hand.put('S', 'K')
    hand.getSuccessor('S', 'K') == None
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.getSuccessor('D', 'A') == Card("S", "2")
    hand.getSuccessor('S', '2') == Card("C", "Q")
    hand.getSuccessor('C', 'Q') == Card("S", "K")
    
def test_deleteRoot():
    hand = PlayerHand()
    assert hand.delete("D", "A") == False
    hand.put("D", "A")
    assert hand.size == 1
    assert hand.delete("D", "A") == True
    assert hand.size == 0
    
def test_deleteLeafNode():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.delete("S", "K") == True
    assert hand.inOrder() == \
"D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 1\n"
    assert hand.preOrder() == \
"D A | 1\n\
S K | 1\n\
S 2 | 1\n\
C Q | 1\n\
H 7 | 1\n\
C K | 1\n"

def test_deleteNodeWithTwoChildren():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.delete("H", "7") == True
    assert hand.inOrder() == \
"D A | 1\n\
S 2 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"
    assert hand.preOrder() == \
"D A | 1\n\
S K | 2\n\
S 2 | 1\n\
C Q | 1\n\
C K | 1\n"
