# PlayerHand.py
from Card import Card

class PlayerHand:
    def __init__(self):
        self.root = None # BST needs reference to the root
        self.size = 0

    def getRoot(self):
        return self.root

    def getTotalCards(self):
        return self.size

    def getMin(self):
        return self._getMin(self.root)

    def _getMin(self, currentNode):
        minval = currentNode
        while minval and minval.left:
            minval = minval.left
        return minval

    def getSuccessor(self, suit, rank):
        card = Card(suit, rank)
        current = self.get(suit, rank)

        if not current:
            return None

        if current.right:

            return self._getMin(current.right)

        elif current.is_left_child():

            return current.parent

        elif current.is_right_child():
            while current and current.is_right_child():

                current = current.parent

            if current.is_left_child():

                return current.parent    

            return None
 
    def put(self, suit, rank):
        if self.root:
            self._put(suit, rank, self.root)
        else:
            self.root = Card(suit, rank)
        self.size += 1

    def _put(self, suit, rank, currentNode):
        putCard = Card(suit, rank)
        if putCard == currentNode:
            currentNode.count += 1
        elif putCard < currentNode:
            if currentNode.left:
                self._put(suit, rank, currentNode.left)
            else:
                currentNode.left = putCard
                putCard.parent = currentNode
        else:
            if currentNode.right:
                self._put(suit, rank, currentNode.right)
            else:
                currentNode.right = putCard
                putCard.parent = currentNode

    def delete(self, suit, rank):
        if self.size > 1:
            removenode = self.get(suit, rank)
            if removenode:
                self.remove(removenode)
                self.size -= 1
                return True
            else:
                return False
        elif self.size == 1 and self.root.suit == suit and self.root.rank == rank:
            self.root = None
            self.size -= 1
            return True
        else:
            return False
    def remove(self, currentNode):
        if currentNode.count > 1:
            currentNode.count -= 1
        elif currentNode.isLeaf(): 
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.has_both_children(): 
            succ = self.getSuccessor(currentNode.suit, currentNode.rank)
            succ.splice_out()
            currentNode.suit = succ.suit
            currentNode.rank = succ.rank
        else: 
            if currentNode.left:
                if currentNode.is_left_child():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.is_right_child():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else:
                    currentNode.replace_node_data(currentNode.left.suit,\
                    currentNode.left.rank, currentNode.left.left,\
                    currentNode.left.right)
            else:
                if currentNode.is_left_child():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.is_right_child():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    currentNode.replace_node_data(currentNode.right.suit,\
                    currentNode.right.rank, currentNode.right.left,\
                    currentNode.right.right)

    def isEmpty(self):
        return self.size == 0
    
    def get(self, suit, rank):
        if self.root:
            res = self._get(suit, rank, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None
    
    def _get(self, suit, rank, currentNode):
        getCard = Card(suit, rank)
        if not currentNode:
            return None
        elif currentNode == getCard:
            return currentNode
        elif getCard < currentNode:
            return self._get(suit, rank, currentNode.left)
        else:
            return self._get(suit, rank, currentNode.right)

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += self._inOrder(currentNode.left)
            ret += str(currentNode)
            ret += self._inOrder(currentNode.right)
        return ret

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += str(currentNode)
            ret += self._preOrder(currentNode.left)
            ret += self._preOrder(currentNode.right)
        return ret
hand = PlayerHand()
hand.put('D', 'A')
hand.put('S', 'K')
hand.put('S', '2')
hand.put('C', 'Q')
hand.put('H', '7')
hand.put('S', 'K')
hand.put('C', 'K')
hand.delete('D', 'A')
print(hand.inOrder())
