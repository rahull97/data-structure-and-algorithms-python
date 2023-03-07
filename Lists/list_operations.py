# create list
li = [10, 20, 30, 'Hello']
print(li)
print("----------------------")

# access elements of list
li = [10, 20, 30, 'Hello']
print(li[1])
print(li[-1])
print("----------------------")

# traverse through list
li = [10, 20, 30, 'Hello']

for el in li:
    print(el)

print("----------------------")

# update element of a list
li = [10, 20, 30]
print(li)
li[1] = 200
print(li)
print("----------------------")

# insert element in a list
li = [10, 20, 30]
print(li)
li.insert(0, 100)
print(li)
print("----------------------")


# append element in a list
li = [10, 20, 30]
print(li)
li.append(40)
print(li)
print("----------------------")

# append another list
li = [10, 20, 30]
li1 = [40, 50, 60]
print(li)
li.extend(li1)
print(li)
print("----------------------")
