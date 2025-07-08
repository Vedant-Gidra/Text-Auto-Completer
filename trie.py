class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def _dfs(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)
        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, result)

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        result = []
        self._dfs(node, prefix, result)
        return result[:10]
