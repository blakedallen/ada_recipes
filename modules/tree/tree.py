
from .tree_node import TreeNode

class Tree():
	""" 
		Tree defines an abstract tree data structure
		Allowing for breadth first search and depth first search
	"""

	def __init__(self, root=None):
		if root == None:
			root = TreeNode(key="root", data=None)
		self.root = root

	def add_node(self, key, data, children={}):
		""" adds a node to the root"""
		tn = TreeNode(key=key, data=data, children=children)
		self.root.add_child(tn)

	def new_node(self, key, data, children={}):
		""" creates and returns a new node"""
		tn = TreeNode(key=key, data=data, children=children)
		return tn

	def dfs(self, key, nodes=None):
		""" given a key will perform depth first search for this key
		"""
		#init
		if nodes == None:
			nodes = [self.root]
		elif len(nodes) == 0:
			return None
		for n in nodes:
			if n.key == key:
				return n
			if n.has_children():
				return self.dfs(key, nodes=n.get_children())
		return None

	def bfs(self, key, nodes=None):
		""" given a key will perform breadth first search
		"""
		if nodes == None:
			nodes = [self.root]
		elif len(nodes) == 0:
			return None
		for n in nodes:
			if n.key == key:
				return n
		for n in nodes:
			if n.has_children():
				return self.bfs(key, nodes=n.get_children())
		return None

