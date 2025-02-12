# values = [-3, -2, 0, 1, 4, -1, 6]
# positive_numbers = list(filter (lambda x:x>0,values))
# print(positive_numbers)

# values = ["Apple", "Banana", "Avocado", "Grapes"]
# new_words = list(filter(lambda x:x.startswith("A"),values))
# print(new_words)

# numbers = [10, 21, 30, 35, 40]
# new_numbers = list(filter(lambda x:x%5==0,numbers))
# print(new_numbers)

# names = ["Alice", "Bob", "Charlie", "David"]
# new_names = list(filter(lambda x: len(x) > 4,names))
# print(new_names)

# letters = ["a", "b", "c", "d", "e", "f"]
# even_indexed = list(filter(lambda x: letters.index(x) % 2 == 0, letters))
# print(even_indexed)


# numbers = [10, 11, 12, 13, 14, 15, 16, 17]
# words =["madam", "apple", "racecar", "python", "level"]
# new_words = list(filter(lambda x:x==x[::-1],words))
# print(new_words)

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n//2):
#         if n%i==0:
#             return False
#     return True

# numbers = [10, 11, 12, 13, 14, 15, 16, 17]
# prime_numbers = list(filter(is_prime,numbers))
# print(prime_numbers)



# students = [
#     {"name": "John", "score": 85},
#     {"name": "Emma", "score": 60},
#     {"name": "Sophia", "score": 90}
# ]

# higest_score = list(filter(lambda student:student["score"]>80,students))
# print(higest_score)


# def contains_vowel(word):
#     vowels = "aeiouAEIOU"
#     return any(char in vowels for char in word)

# words = ["sky", "apple", "dry", "orange", "fly"]
# words_with_vowels = list(filter(contains_vowel, words))
# print(words_with_vowels)
