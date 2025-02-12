# append()	Adds an element at the end of the list
# extend()	Adds multiple elements from another iterable (list, tuple, set, etc.)
# insert()	Inserts an element at a specific position
# remove()	Removes the first occurrence of a specified element
# pop()	    Removes and returns an element at a specific index (default is last)
# clear()	Removes all elements from the list
# index()	Returns the index of the first occurrence of an element
# count()	Returns the number of times an element appears in the list
# sort()	Sorts the list in ascending order (default) or descending
# reverse()	Reverses the order of elements in the list
# copy()	Returns a shallow copy of the list



# list1=[1,2,3,4]
# list2=[5,6,7]
# list1.extend(list2)
# print(list1)

# value = ["Java", "C++", "JavaScript"]
# value.insert(1,"Python")
# print(value)

# value = [5, 10, 15, 20]
# value.remove(5)
# print(value)

# value = [1, 2, 3, 4, 5]
# value.pop()
# print(value)

# arr = ["banana", "apple", "cherry"]
# idx = arr.index("apple")
# print(idx)

# value = [1, 2, 2, 3, 4, 2, 5]
# n = value.count(2)
# print(n)

# value =[4, 2, 9, 1]
# value.sort()
# print(value)

# value = ["a", "b", "c", "d"]
# value.reverse()
# print(value)

# value = [100, 200, 300]
# newValue = value.copy()
# print(newValue)


# def remove_even(arr):
#     result = []
#     for i in arr:
#         if i%2!=0:
#             result.append(i)
#     return result

# arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 8]
# print(remove_even(arr))


# def ins(arr):
#     idx=0
#     for i in range(len(arr)):
#         if arr[i] == "JavaScript":
#             arr.insert(idx,"Python")
#             idx+=1
#         idx+=1
#     return arr
# arr = ["C", "Java", "JavaScript"]
# print(ins(arr))


# words = ["apple", "hi", "banana"]
# words.sort(key=len)
# print(words)
