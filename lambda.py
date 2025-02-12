add = lambda x,y : x+y
print(add(2,4))

sqr = lambda x:x*x
print(sqr(5))

even_odd = lambda x:x%2==0
print(even_odd(3))

mul = lambda x,y:x*y
print(mul(4,5))


val = [1, 2, 3, 4, 5]
result = list(map(lambda x:x*x,val))
print(result)


conversion = lambda s:s.lower()
print(conversion("Jello"))