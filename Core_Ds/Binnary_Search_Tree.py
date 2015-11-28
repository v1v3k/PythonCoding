#Creating a Binary Search Tree(BST) from a Sorted Python List


class binaryNode:
     def __init__(self,data,left,right):
         self.data = data
         self.right = right
         self.left = left
         self.count = 1;


class binaryTree:
     def __init__(self):
         self.root = None


     def createBinSearchTree(self,L,low, high):
         """
         Precondition: List L is sorted
         PostCondition: root of binary search tree is returned
         """
         if low <= high:
             middle = (low+high)/2
             newBinaryNode = binaryNode(L[middle],None,None)
             newBinaryNode.left = self.createBinSearchTree(L,low,middle-1)
             newBinaryNode.right = self.createBinSearchTree(L,middle+1,high)
             return newBinaryNode
         else: return None


     def treeSearch(self,key):
         return self.recTreeSearch(self.root,key)

     def recTreeSearch(self,r,key):
       if r != None:
           if r.data == key:
                    return r.data
           else :
               if r.data > key: return self.recTreeSearch(r.left,key)
               else:  return self.recTreeSearch(r.right,key)
       else: return None

     def inOrderPrint(self,r):
         if r != None:
              self.inOrderPrint(r.left)
              print r.data
              self.inOrderPrint(r.right)


     def insert(self,data):
         self.root = self.recInsert(self.root,data)

     def recInsert(self,r,data):
        if r == None:
             newNode = binaryNode(data,None,None)
             r = newNode
        elif data == r.data:
              r.count = r.count + 1
        elif data<r.data:
              r.left = self.recInsert(r.left,data)
        else:
              r.right = self.recInsert(r.right,data)
        return r

     def removeNode(self,r):
        toRemove = r
        if r == None:
             return None
        elif r.right == None:
             r = r.left
        elif r.left == None:
              r = r.right
        else:
              parent = r
              toRemove = r.left
              while toRemove.right !=  None:
                    parent = toRemove
                    toRemove = toRemove.right
              r.data = toRemove.data
              if parent == r:
                   parent.left = toRemove.left
              else:
                   parent.right = toRemove.left
        return r

     def remove(self,key):
        self.root = self.recRemove(self.root,key)

     def recRemove(self, r, key):
         if r == None or  r.data == key:
              return self.removeNode(r)
         elif r.data > key:
              r.left = self.recRemove(r.left,key)
         else:
              r.right =  self.recRemove(r.right,key)
         return r

def tester():
    L = [3,5,7,15,16,24,57]
    bst = binaryTree()
    bst.root = bst.createBinSearchTree(L,0,len(L)-1)
    bst.inOrderPrint(bst.root)
    print
    bst.remove(15)
    bst.inOrderPrint(bst.root)
    print
    bst.insert(17);
    bst.inOrderPrint(bst.root)
    print
    bst.insert(2);
    bst.inOrderPrint(bst.root)
    print
    bst.insert(70);
    bst.inOrderPrint(bst.root)
    print
    bst.remove(2)
    bst.inOrderPrint(bst.root)
    print
    bst.remove(70)
    bst.inOrderPrint(bst.root)
    print



if __name__ == '__main__':
    tester()





