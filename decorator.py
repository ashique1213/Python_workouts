# def print_message_decorator(func):
#     def wrapper():
#         print("Function is called")
#         return func()
#     return wrapper

# @print_message_decorator
# def greet():
#     print("Hello, World!")

# greet()



# import time

# def decorator_function(func):
#     def wrap():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end-start)
#     return wrap

# @decorator_function
# def main():
#     time.sleep(1)
#     print("Exicuted")

# main()



# def upper_case(func):
#     def wrapper():
#         return func().upper()
#     return wrapper

# @upper_case
# def say_hello():
#     return "hello"

# print(say_hello())


# def decorator(func):
#     def wrap():
#         val1 = func()
#         val2 = int(input("Enter number B: "))
#         return  val1 + val2
#     return wrap
    
# @decorator
# def sum_of():
#     return int(input("Enter number A: "))

# print(sum_of())  