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

#matrix
my_matrix =[
  [1,0,9],
  [2,46,5],
  [5,66,6]
]

print(my_matrix[1][1])


# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
'''find Oranges'''
print('''find Oranges''')
print(basket[1][1][0])



#Bulit in list function 
sample_list =[1,2,3,4,5]

#append add the value in last 
sample_list.append(100)
my_list = sample_list
print(my_list)
print('----------------')
#add value with Index

sample_list.insert(3,300)
index_val = sample_list
print(index_val)
print('----------------')

#extends
index_val.extend([101,109])
my_ext = index_val
print(my_ext)
print('----------------')

#pop normal 
print(my_ext.pop())
print(my_ext)
print('----------------')

#pop with index 
print(my_ext.pop(3))
print(my_ext)
print('----------------')

#remove the Value
my_ext.remove(5)
print(my_ext)
print('----------------')

#copy 
my_listCopy = my_ext.copy()
print(my_listCopy)
print('----------------')

#clear
my_ext.clear()
print(my_listCopy)
print(my_ext)
print('----------------')