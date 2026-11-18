"""
Real-world use:
Trie → Autocomplete and prefix-based search.

Search bars can store words character-by-character.
When the user types a prefix like "ca", we can follow
the "c" → "a" path and find matching words.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_word = True

    def starts_with(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


trie = Trie()

trie.insert("car")
trie.insert("cat")
trie.insert("camera")
trie.insert("cake")

print(trie.starts_with("ca"))   # True
print(trie.starts_with("cam"))  # True
print(trie.starts_with("dog"))  # False