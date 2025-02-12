
# Create a dictionary using **dictionary comprehension**, where keys are numbers from `1 to 5` and values are their squares.  

new_dict = {k:k*k for k in range(1,5)}
print(new_dict)

# Given a list `[10, 20, 30]`, create a dictionary where the keys are the numbers and the values are their double.

# value = [10, 20, 30]
# new_dict = {k:k*k for k in value}
# print(new_dict)


#  Create a dictionary from a string `"hello"`, where keys are characters and values are their ASCII values. 


# Create a dictionary where keys are numbers from `1 to 5`, and values are `"even"` or `"odd"`, depending on the number.

# new_dict = {k:"even" if k%2==0 else "odd" for k in range(1,6)}
# print(new_dict)  


# Given a list `["apple", "banana", "cherry"]`, create a dictionary where the key is the word, and the value is its length.  

# value = ["apple", "banana", "cherry"]
# new_dict = {k:len(k) for k in value}
# print(new_dict)

# Given a dictionary `{ "a": 1, "b": 2, "c": 3, "d": 4 }`, create a new dictionary where values are squared using dictionary comprehension.  

# values = { "a": 1, "b": 2, "c": 3, "d": 4 }
# new_dict = {k:v*v for k,v in values.items()}
# print(new_dict)


# Convert a list of tuples `[("name", "Alice"), ("age", 25), ("city", "New York")]` into a dictionary using dictionary comprehension.  

# values = [("name", "Alice"), ("age", 25), ("city", "New York")]
# new_dict = {k:v for k,v in values}
# print(new_dict)


# Given two lists `["a", "b", "c"]` and `[1, 2, 3]`, create a dictionary where the first list contains keys and the second contains values.  

# val=["a", "b", "c"]
# val2=[1, 2, 3]

# new_dict = {val[i]:val2[i] for i in range(len(val)) }
# print(new_dict)

# Filter a dictionary `{ "a": 10, "b": 20, "c": 5, "d": 40 }` to keep only key-value pairs where values are greater than `15`.  

# values = { "a": 10, "b": 20, "c": 5, "d": 40 }

# new_dict = {k:v for k,v in values.items() if v<15}
# print(new_dict)

#  Given a sentence `"hello world"`, create a dictionary where keys are words and values are their lengths.  

sentence = "hello world"
new_values = {k:len(k) for k in sentence.split() }
print(new_values)


