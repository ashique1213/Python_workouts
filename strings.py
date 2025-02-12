
# upper(), lower(), title(), capitalize(), swapcase()
# def conv(s):
#     return s.upper()

# h="hello"
# print(conv(h))

# def conv(s):
#     return s.title()

# h="hello"
# print(conv(h))


# def swaping(s):
#     new=''
#     for i in s:
#         if i != i.upper():
#             new+=i.upper()
#         else:
#             new+=i.lower()
#     return new

# value ="HeLLo WoRLd"
# print(swaping(value))

# print(value.swapcase())


# user_input = input("Enter a word: ")
# if user_input.upper() == "HELLO":
#     print("Match!")
# else:
#     print("No match!")



# isalpha(), isdigit(), isalnum(), isspace(), islower(), isupper()
# def alpha(s):
#     if s.isalpha():
#         return True
#     return False

# value ="jljdlsk1"
# print(alpha(value))

# def alpha(s):
#     if s.isdigit():
#         return True
#     return False

# value ="1234h"
# print(alpha(value))



# find(), rfind(), index(), replace()

# s = "Hello world"
# position = s.find("w")
# print(position)

# s = "Hello world"
# new_s= s.replace("world","ashique")
# print(new_s)


# def replace_vow(s):
#     vowels="aeiou"
#     for vowel in vowels:
#         s = s.replace(vowel,"*")
#     return s

# sentence = "Hello, how are you?"
# print(replace_vow(sentence))


# split(), rsplit(), splitlines(), join(),strip()


# sentence = "apple,banana,grape"
# new_sentence = sentence.split(",")
# print(new_sentence)


# values = ["Hello", "World"]
# newValue  = " ".join(values)
# print(newValue)

# startswith(), endswith()


# Write a program to find and print the longest word in "Python is fun and amazing" 
# (split the sentence into words and check their lengths).

# def longest(s):
#     value = s.split(" ")
#     length=0
#     for i in value:
#         if len(i)>length:
#             length=len(i)
#     return length

# s="Python is fun and amazing"
# print(longest(s))


# Remove all duplicate characters from "banana" and print the result.

# def duplicates(s):
#     result =" "
#     for i in s:
#         if i not in result:
#             result+=i
#     return result

# s = "banana"
# print(duplicates(s))


# Convert the sentence "this is python" into "This Is Python" without using .title().

# def cap(s):
#     value = s.split()
#     result=" "
#     for i in value:
#         result += i.capitalize()
#     return "".join(result)

# s="this is python"
# print(cap(s))


# Find out how many words are in "Python is great for beginners".

# def count(s):
#     value = s.split()
#     return len(value)

# value ="Python is great for beginners"
# print(count(value))


#  Remove all special characters (!@#$%^&*) from "Hello@World!123".

# def removespecial(s):
#     result=""
#     for i in s:
#         if i.isalpha():
#             result+=i
#     return result

# value ="Hello@World!123"
# print(removespecial(value))

# Count the number of uppercase and lowercase letters in "PyThOn Is FuN".

# def countupper(s):
#     upper=0
#     lower=0
#     for i in s:
#         if i==i.upper() and i != " ":
#             upper+=1
#         else:
#             lower+=1
#     return upper,lower

# value="PyThOn Is FuN"
# print(countupper(value))


# Reverse the string "hello world" without using loops.

# value="hello world"
# print(value[::-1])


