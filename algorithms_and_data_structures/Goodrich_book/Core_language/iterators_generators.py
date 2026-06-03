# Iterators and iterables
lists = [[1,2,3], [4,5,6], [7,8,9]]

for sublist in lists:
    #sublist is an iteratot of the iterable lists
    for item in sublist:
        print(item)

# for sublist in lists:
#     print(sublist)

# for item in lists:
#     print(item)

# for sublist in lists:
#     print(sublist)

i = iter(lists)
print(next(i))
print(next(i))
print(next(i))

#Generators: yield statement returns a next value to the caller. Yield is not to be combined with return
# and serves a pupose of creating generators
#Python generators are quite convenient as they allow you to generate a sequence of values over time, without having to store all the values in memory.
def factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i
factor = factors(100)
print(next(factor))
print(next(factor))
print(next(factor))
print(next(factor))
print(next(factor))
print(next(factor))
print(next(factor))

def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b
fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))