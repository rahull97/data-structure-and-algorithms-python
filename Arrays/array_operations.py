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
