class Hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key,value])

    
    def lookup(self,key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self,key):
        index = self.hash_function(key)
        for i,pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def update(self,key,new_value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = new_value
                return True
        return None
    
    def exist(self,key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0]==key:
                return
    
    def display(self):
        for i,pair in enumerate(self.table):
            print(f"index{i}:{pair}")

ht = Hashtable(10)
ht.insert("apple",10)
ht.insert("elppa",20)
ht.insert("mango",70)
ht.display()
ht.insert("elppa",20)
value = ht.lookup("mango")
print(value)
ht.update("apple",50)
ht.display()
