#!/usr/bin/env python

class Node:

	def __init__(self,val):

		self.value = val 
		self.left = None 
		self.right = None 


def isMirror(root1,root2):

	if root1 is None and root2 is None:
		return True 

	if root1 is not None and root2 is not None:
		if root1.value == root2.value:

			return (isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left))


	return False

def isSymmetric(root):

	return isMirror(root,root)



root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print "1" if isSymmetric(root) == True else "0"


