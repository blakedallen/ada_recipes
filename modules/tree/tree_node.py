
class TreeNode():
	def __init__(self, key="", data=None, children={}):
		self.key = key
		self.data = data
		self.children = children
		
	def add_child(self, node):
		self.children[node.key] = node

	def has_child(self, key):
		return key in self.children

	def get_child(self, key):
		return self.children[key]

	def del_child(self, key):
		del self.children[key]
		return key

	def has_children(self):
		return len(self.children) > 0

	def get_children(self):
		""" get a list of nodes"""
		return self.children.values()

	def set_children(self, children):
		if typeof(children) == list:
			for c in children:
				self.add_child(c)
		elif typeof(children) == dict:
			self.children = children
		else:
			raise Exception("Error, set_children requires either a list of TreeNode or Dict of TreeNode.key --> TreeNode")

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data
