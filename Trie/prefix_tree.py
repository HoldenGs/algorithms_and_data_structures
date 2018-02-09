#!/usr/bin/env python3

from collections import defaultdict


class TrieNode:
	def __init__(self):
		self.children = defaultdict(TrieNode)
		self.is_eow = False


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		tmp = self.root
		for c in word:
			if tmp.children[c] is False:
				tmp.children[c] = {c: TrieNode}
			tmp = tmp.children[c]
		tmp.is_eow = True

	def search(self, prefix):
		ret_list = []
		stk = []
		tmp = self.root
		for c in prefix:
			tmp = tmp.children[c]
		stk.append((tmp.children, prefix))
		while stk:
			top, word = stk.pop()
			for c, node in top.items():
				if node.is_eow:
					ret_list.append(word + c)
				stk.append((node.children, word + c))
		return ret_list


if __name__ == "__main__":
	prefix_tree = Trie()
	prefix_tree.insert('hello')
	prefix_tree.insert('help')
	prefix_tree.insert('helper')

	search_string = 'hel'
	result = str(prefix_tree.search(search_string))

	print("Search: " + search_string)
	print("Found: " + result)
