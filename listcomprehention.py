# Create a list of squares of numbers from 1 to 10.

# arr = [i*i for i in range(1,11)]
# print(arr)

# Generate a list of even numbers from 1 to 20.

# arr = [i for i in range(1,21) if i%2==0]
# print(arr)

# Convert a list of temperatures from Celsius to Fahrenheit (C * 9/5 + 32).

# arr =  [5, 10, 15, 20, 25, 30]
# new_arr = [i * 9/5 + 32 for i in range(len(arr))]
# print(new_arr)

# Create a list that contains only positive numbers from [-4, -2, 0, 3, 7, -1, 10].

# arr = [-4, -2, 0, 3, 7, -1, 10]
# new_arr = [i for i in arr if i>0]
# print(new_arr)


# Extract the first letter of each word in ["apple", "banana", "cherry"]

# arr = ["apple", "banana", "cherry"]
# new_arr = [i[:1] for i in arr]
# print(new_arr)


#  Convert a list of words to uppercase: ["hello", "world", "python"] → ["HELLO", "WORLD", "PYTHON"].

# arr=["hello", "world", "python"]
# new_arr = [i.upper() for i in arr]
# print(new_arr)


#  Replace all negative numbers in [3, -1, 5, -7, 9, -2] with 0.

# arr = [3, -1, 5, -7, 9, -2]
# new_arr = [0 if i<0 else i for i in arr]
# print(new_arr)

#  Find the length of each word in ["cat", "elephant", "tiger"].

# arr = ["cat", "elephant", "tiger"]
# new_arr = [len(i) for i in arr]
# print(new_arr)

#  Filter out words that contain the letter 'a' from ["apple", "banana", "cherry", "date", "fig"].

# arr = ["apple", "banana", "cherry", "date", "fig"]
# new_arr = [i for i in arr if "a" in i]
# print(new_arr)

# Create a list of tuples where each tuple contains a number and its square (1, 1), (2, 4), ... for numbers 1 to 5.

# arr = [(i,i*i) for i in range(1,6)]
# print(arr)

# Flatten a nested list [[1, 2], [3, 4], [5, 6]] into [1, 2, 3, 4, 5, 6].

# arr = [[1, 2], [3, 4], [5, 6]] 
# new_arr = [j for i in arr for j in i]


# Extract vowels from a string "hello world" → ["e", "o", "o"].

# s ="hello world"
# arr = [i for i in s if i in "aeiou"]
# print(arr)


# Replace all occurrences of "dog" with "cat" in ["dog", "rabbit", "dog", "fish"].

# arr = ["dog", "rabbit", "dog", "fish"]
# new_arr = [i if i!="dog" else "cat" for i in arr]
# print(new_arr)

# Generate a list of numbers from 1 to 20 where even numbers are squared and odd numbers are tripled.

# arr = [i*i if i%2==0 else i**i for i in range(1,5)]
# print(arr)

# Create a new list from [1, 2, 3, 4, 5] where elements greater than 3 are doubled and others remain the same.

# arr =[1, 2, 3, 4, 5]
# new_arr = [i*i if i>3 else i for i in arr]
# print(new_arr)

