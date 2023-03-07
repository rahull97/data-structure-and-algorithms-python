import numpy as np

# create two dimensional array
two_d_array = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)
print(two_d_array)
print("------------------------")

# insert row or column in a 2d array
two_d_array = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)

# adds new column at the 0th position
new_two_d_array = np.insert(two_d_array, 0, [[100, 110, 120]], axis=1)
print(new_two_d_array)

# adds new row at the 1st position
new_two_d_array = np.insert(two_d_array, 1, [[100, 110, 120]], axis=0)
print(new_two_d_array)
print("------------------------")

# append row or column in a 2d array
two_d_array = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)

# append new column
new_two_d_array = np.append(two_d_array, [[100], [110], [120]], axis=1)
print(new_two_d_array)

# append new row
new_two_d_array = np.append(two_d_array, [[100, 110, 120]], axis=0)
print(new_two_d_array)
print("------------------------")

# access an element of 2d array
two_d_array = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)

# access it using <array_name>[row_index][col_index]
print(two_d_array[1, 1])
print(two_d_array[2, 1])
print(two_d_array[0, 1])
print("------------------------")

# traverse 2d array
two_d_array = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)

for row_idx in range(len(two_d_array)):
    for col_idx in range(len(two_d_array[0])):
        print(two_d_array[row_idx][col_idx], end="|")
    print()
print("------------------------")


# search for an element in 2d array
def search_element(arr, key):
    for row_idx in range(len(arr)):
        for col_idx in range(len(arr[0])):
            if arr[row_idx][col_idx] == key:
                return (row_idx, col_idx)
    return -1


two_d_array = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)
print(search_element(two_d_array, 30))
print(search_element(two_d_array, 100))
print("------------------------")

# delete row or column from 2d array
two_d_array = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)

# delete row at index 1
new_two_d_array = np.delete(two_d_array, 1, axis=0)
print(new_two_d_array)

# delete column at index 2
new_two_d_array = np.delete(two_d_array, 2, axis=1)
print(new_two_d_array)
print("------------------------")
