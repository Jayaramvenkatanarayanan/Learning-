# list
my_list = ['a', 'b' 'Hello', True, None, 23]
print('List', my_list)
print('get induval')
print(my_list[3])
print(my_list[-1])


#List Slicing
my_list1 = ['a', 'b', 'Hello', True, None, 23]

print('List Slicing')
print(my_list1[::2])

#AddList
my_list2 = ['a', 'b', 'Hello', True, None, 23]
print('AddList')
my_list2[1] = 'jayaram'
print(my_list2)

#copyList
print('copyList')
my_list_copy = my_list1[:]
print(my_list_copy)