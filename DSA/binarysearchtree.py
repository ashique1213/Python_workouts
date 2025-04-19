class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.value,end=' ')
            self.in_order(node.right)

    def pre_order(self,node):
        if node:
            print(node.value,end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    def post_order(self,node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value,end=' ')
    
    def delete(self,node,value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete(node.left,value)
        elif value>node.value:
            node.left = self.delete(node.right,value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self.find(node.right)
            node.value = min_node.value
            node.right = self.delete(node.right,min_node.value)
        
        return node
    
    def height(self,node):
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left,right)
    
    def search(self,value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def sum_of(self,node):
        if node is None:
            return 0
        return node.value + (self.sum_of(node.left)+self.sum_of(node.right))
    

    def depth(self,node,target,current_depth=0):
        if node is None:
            return -1
        if node.value == target:
            raise current_depth
        elif target < node.value:
            return self.depth(node.left,target,current_depth+1)
        else:
            return self.depth(node.right,target,current_depth+1)
        
    def largest(self,node):
        if node is None:
            return None
        current = node
        while current.right:
            current = current.right
        return current.value
    
    def count(self,node):
        if node is None:
            return 0
        left = self.count(node.left)
        right = self.count(node.left)
        return 1+left+right
    
    def second_largest(self,node):
        if node is None or (node.left is None and node.right is None):
            return None
        parent = None
        current = node

        while current.right:
            parent = current
            current = current.right
        
        if current.left:
            temp = current.left 
            while temp.right:
                temp = temp.right
            return temp.value
        
        return parent.value if parent else None

    def find_closest(self, node, target):
        closest = node.value  # Start with root value
        current = node

        while current:
            if abs(target - current.value) < abs(target - closest):
                closest = current.value  # Update closest value if current is nearer

            if target < current.value:
                current = current.left  # Move left
            elif target > current.value:
                current = current.right  # Move right
            else:
                break  # If exact match is found, return immediately

        return closest


bt = BST()
# Insert Values
bt.insert(10)
bt.insert(3)
bt.insert(6)
bt.insert(7)
bt.insert(15)
bt.insert(12)
bt.insert(18)
bt.insert(17)
bt.insert(20)

# In-order Traversal (Should print: 3 6 7 10 12 15 17 18 20)
print("In-Order Traversal:")
bt.in_order(bt.root)
print()

# Pre-order Traversal (Should print: 10 3 6 7 15 12 18 17 20)
print("Pre-Order Traversal:")
bt.pre_order(bt.root)
print()

# Post-order Traversal (Should print: 7 6 3 12 17 20 18 15 10)
print("Post-Order Traversal:")
bt.post_order(bt.root)
print()

# Find the largest value (Should return: 20)
print("Largest:", bt.largest(bt.root))

# Find the second largest value (Should return: 18)
print("Second Largest:", bt.second_largest(bt.root))

# Closest value tests
print("Closest to 8:", bt.find_closest(bt.root, 8))   # Should return: 7
print("Closest to 16:", bt.find_closest(bt.root, 16)) # Should return: 15 or 17
print("Closest to 19:", bt.find_closest(bt.root, 19)) # Should return: 18 or 20

# Sum of all nodes (Should return: 108)
print("Sum of all nodes:", bt.sum_of(bt.root))

# Height of the tree (Should return: 3)
print("Height of tree:", bt.height(bt.root))

# Search for a value
print("Search 15:", bt.search(15)) # Should return: True
print("Search 100:", bt.search(100)) # Should return: False
