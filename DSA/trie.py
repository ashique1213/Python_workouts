class Trienode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False
    
class Trie:
    def __init__(self):
        self.root = Trienode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trienode()
            node = node.children[char]
        node.is_end_word = True
    
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    

    def start_with(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return self.collect(node,prefix)
    
    def collect(self,node,prefix):
        word = []
        if node.is_end_word:
            word.append(prefix)
        for char,childnode in node.children.items():
            word.extend(self.collect(childnode,prefix+char))
        return word
    

trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat") 
trie.insert('apricot')
print(trie.autocomplete("ap"))  
# Output: ['app', 'apple', 'apricot']
# print(trie.autocomplete("bat"))  # Output: ['bat', 'batman']
# print('starts with',trie.start_with('e'))