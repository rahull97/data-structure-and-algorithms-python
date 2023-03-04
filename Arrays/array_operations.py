import array


# create array
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])
print(arr1)
arr2 = array.array('d', [1.1, 1.2, 1.4])
print(arr2)
print("-----------------------")

# insert an element in an array
arr1 = array.array('i', [10, 20, 30])
arr1.insert(3, 40)
print(arr1)
arr1.insert(0, 50)
print(arr1)
arr1.insert(2, 60)
print(arr1)
print("-----------------------")

# traverse an array
arr1 = array.array('i', [10, 20, 30, 40])

for el in arr1:
    print(el)

for idx, el in enumerate(arr1):
    print(f"index: {idx} and value: {el}")
print("-----------------------")

# access an element of an array
arr1 = array.array('i', [10, 20, 30])
print("element at Oth index:", arr1[0])
print("element at 1st index:", arr1[1])
print("element at 2nd index:", arr1[2])
print("-----------------------")


# search for an element in an array
def search_element(arr, key):
    for idx, el in enumerate(arr):
        if el == key:
            return idx
    return -1


arr1 = array.array('i', [10, 20, 30])
print(search_element(arr1, 110))
print("-----------------------")

# delete an element from array
arr1 = array.array('i', [10, 20, 10, 40])
arr1.remove(10)
print(arr1)
print("-----------------------")

# print array buffer information
arr1 =  array.array('i', [10, 20, 30, 40])
print(arr1.buffer_info())
print("-----------------------")

# convert array to list
arr1 = array.array('i')
arr1.append(10)
arr1.append(100)
print(arr1)
print(arr1.tolist())
print("-----------------------")

# extend array with another array
arr1 = array.array('i', [10,20,30])
arr2 = array.array('i', [40,50,60])
arr1.extend(arr2)
print(arr1)
print("-----------------------")

# pop element from an array
arr1 = array.array('i', [10, 20, 30])
el = arr1.pop() # pops last element
print(el)
el = arr1.pop(0) # pops element at the given index
print(el)
print(arr1)
print("-----------------------")
