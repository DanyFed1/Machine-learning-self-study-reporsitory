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