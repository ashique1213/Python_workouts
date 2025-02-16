# def fac(n):
#     if n==0:
#         return 1
#     else:
#         return n*fac(n-1)
    
# print(fac(5))

# def fibo(n):
#     if n<=1:
#         return n
#     else:
#          return fibo(n-1)+fibo(n-2)
    
# print(fibo(6))


# def sum_of(n):
#     if n==0:
#         return n
#     else:
#         return n%10 + sum_of(n//10)
# print(sum_of(123))

# def reverse(s):
#     if len(s)==1:
#         return s
#     else:
#         return reverse(s[1:])+s[0]
    
# print(reverse("hello"))


# def sum_of_num(n):
#     if n==0:
#         return n
#     else:
#         return n+sum_of_num(n-1)
    
# print(sum_of_num(10))



def binary_search(arr,low,high,x):
    if high >= low:
        mid = high+low // 2
        if arr[mid] == x:
            return mid   
        if arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    return -1  

arr = [1, 3, 5, 7, 9, 11, 13, 15]
x = 7

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")


