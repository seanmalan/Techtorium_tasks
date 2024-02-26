unique_id = {123, 234, 345, 456}


print(2 in unique_id)
print(123 in unique_id)

  
id1 = 2 in unique_id
id2 = 123 in unique_id

if id1 == True:
  print("This ID is already taken")
else:
  print("This ID is available")
  
if id2 == True:
  print("This ID is already taken")
else:
  print("This ID is available")
  


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 8, 9, 10]
common = []

def common_elements(list1, list2):
  for i in list1:
    for j in list2:
      if i == j:
        common.append(i)
        print(common)
        
print(common)


common_elements(list1, list2)

list3 = [1, 2, 3, 4, 5]
list4 = [4, 5, 8, 9, 10]



#Implement a Python function that takes two lists and returns a set containing only the common elements between them. Print the resulting set.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 8, 9, 10]

def common_elements(list1, list2):
  return set(list1) & set(list2)

print(common_elements(list1, list2))
#Output: {4, 5}


list1 = {1, 2, 3, 4, 5, 6, 781}
list2 = {4, 5, 6, 781, 8, 9, 10}
common_ids = list1.intersection(list2)

print(common_ids)


