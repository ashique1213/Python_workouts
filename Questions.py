# # Find Duplicate Elements in a List

# def duplicates(arr):
#     duplicates = set()
#     unique = set()
#     for num in arr:
#         if num in unique:
#             duplicates.add(num)
#         unique.add(num)
#     return list(duplicates)

# values = [1, 2, 3, 2, 4, 5, 1]

# print(duplicates(values))


#  Find Missing Number in an Array (1 to N)

# def missing_numbers(arr):
#     n = len(arr) +1
#     result = n*(n+1)//2 - sum(arr)
#     return result
# values = [1, 2, 3, 5]
# print(missing_numbers(values))


# def merge_sort(l1,l2):
#     i=0
#     j=0
#     merged = []
#     while i < len(l1) and j < len(l2):
#         if l1[i] < l2 [j]:
#             merged.append(l1[i])
#             i+=1
#         else:
#             merged.append(l2[j])
#             j+=1
#     merged.extend(l1[i:])
#     merged.extend(l2[j:])
#     return merged


# arr1=[1, 3, 5]
# arr2=[4, 7, 6]
# print(merge_sort(arr1,arr2))