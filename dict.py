# | `dict.clear()` | Removes all items from the dictionary. |
# | `dict.copy()` | Returns a shallow copy of the dictionary. |
# | `dict.fromkeys(seq, value)` | Creates a new dictionary from a sequence of keys and assigns a common value to all keys. |
# | `dict.get(key, default)` | Returns the value of a key if it exists; otherwise, returns the default value. |
# | `dict.items()` | Returns a view object of key-value pairs. |
# | `dict.keys()` | Returns a view object of all keys in the dictionary. |
# | `dict.values()` | Returns a view object of all values in the dictionary. |
# | `dict.pop(key, default)` | Removes and returns the value of the given key. If the key does not exist, returns the default value. |
# | `dict.popitem()` | Removes and returns the last key-value pair from the dictionary. |
# | `dict.update(other_dict)` | Updates the dictionary with key-value pairs from another dictionary. |
# | `dict.setdefault(key, default)` | If key exists, returns its value. If not, inserts key with the default value. |


# dictionary ={
#     "name":"ashique",
#     "place":"Wayanad"
# }

# print(dictionary)

# value = dictionary.get("name","None")
# print(value)

# value2 = dictionary.items()
# print(value2)

# value3 = dictionary.keys()
# print(value3)

# value4 = dictionary.values()
# print(value4)

# value5 = dictionary.pop("e","There is no field")
# print(value5)

# # dictionary.popitem()
# print(dictionary)

# dictionary2={
#     "job":"SEO"
# }

# dictionary.update(dictionary2)
# print(dictionary)


# details = {"name": "Alice", "age": 25, "city": "New York"}
# value = details.get("age","None")
# print(value)

# details ={1: "one", 2: "two", 3: "three"}
# keys = details.keys()
# values = details.values()
# print(keys)
# print(values)

# details = { "name": "Alice", "age": 25, "city": "New York" }
# details.pop("city","None")
# print(details)



# keys = ["a", "b", "c"]
# value = 0
# new_dict = dict.fromkeys(keys,value)
# print(new_dict)


# person = { "name": "Alice", "age": 25 }
# person.setdefault("gender","female")
# print(person)

# def rev_gre(data):
#     for k,v in data.items():
#         if v>50:
#             data.pop(k)
#     return data

# data = { "a": 10, "b": 55, "c": 42, "d": 100 }
# print(rev_gre(data))


# def highest(sal):
#     highest=0
#     for k,v in sal.items():
#         if v>highest:
#             highest=v
#     return highest


# salary ={ "Alice": 5000, "Bob": 7000, "Charlie": 6000 }
# print(highest(salary))

#  Count character frequency in a string using .get()
text = "banana"
count = {}
for i in text:
    count[i]=count.get(i,0)+1
print(count)


# Merge two dictionaries without .update()

dict1 = { "a": 1, "b": 2 }
dict2 = { "c": 3, "d": 4 }

merged = {**dict1,**dict2}
print(merged)


# Remove duplicate values from a dictionary

data = { "a": 10, "b": 20, "c": 10, "d": 30 }
unique_values = {}

for k,v in data.items():
    if v not in unique_values.values():
        unique_values[k]=v
print(unique_values)



# Print only employee names from a nested dictionary
# employees = {
#     "emp1": {"name": "Alice", "age": 25, "dept": "HR"},
#     "emp2": {"name": "Bob", "age": 30, "dept": "IT"},
#     "emp3": {"name": "Charlie", "age": 28, "dept": "Finance"},
# }

# for v in employees.values():
#     print(v["name"])