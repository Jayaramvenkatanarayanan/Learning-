#Filter 
# random list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(None, randomList)


for items in filteredList:
  print(items)