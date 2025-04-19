class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)

    def insert_bottom(self,data):
        if len(self.stack)==0:
            self.stack.append(data)
        else:
            temp = self.stack.pop()
            self.insert_bottom(data)
            self.stack.append(temp)
    
    def pops(self):
        if len(self.stack)==0:
            print("empty")
            return None
        else:
            return self.stack.pop()
    
    def peek(self):
        if len(self.stack)==0:
            print("empty")
            return
        else:
            return self.stack[-1]

    def length(self):
        print('length is :',len(self.stack)) 

    def reverse(self):
        if len(self.stack)==0 : 
            return
        temp = self.stack.pop()
        self.reverse()
        self.insert_bottom(temp)


    def sort(self):
        temp_stack = Stack()
        while len(self.stack) > 0:
            current = self.pops()  
            while len(temp_stack.stack) > 0 and temp_stack.peek() > current:  
                self.push(temp_stack.pops())
            temp_stack.push(current)
        while len(temp_stack.stack) > 0:
            self.push(temp_stack.pops())

    def display(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            print('stack = ',self.stack) 


stk = Stack()
stk.push(3)
stk.push(4)
stk.push(6)
stk.push(7)
stk.display()
stk.insert_bottom(4)
stk.display()
stk.pops()
stk.display()
stk.peek()
stk.reverse()
stk.display()
