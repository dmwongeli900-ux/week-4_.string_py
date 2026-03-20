arr = [10, 20, 30, 40]

# Insert
i = int(input("Insert position: "))
v = int(input("Value: "))
arr.insert(i, v)
print("After insert:", arr)

# Delete
d = int(input("Delete position: "))
arr.pop(d)
print("After delete:", arr)