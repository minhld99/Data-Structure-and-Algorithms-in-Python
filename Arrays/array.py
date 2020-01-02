# ---------------------------- Arrays -------------------------------

arr = [1,2,3,4,5]
print("Array is: ", arr)

# --------------- Random Indexing -> O(1) complexity ----------------
# ----------- if we know index of item to get from array ------------

print("Second Element of Array is: ", arr[1])

# ------------------- Insert item at given index --------------------

arr[1] = 200
print("Array[1] after being changed: ", arr[1])

# ------------------ Print all array in diff way --------------------

print("Print all items in array using num:")
for num in arr:
    print(num)

print("Print all items in array using index: ")
for i in range(len(arr)):
    print(arr[i])

print("Print out items from starting to ending index: ", arr[0:2])

print("Print out whole array using ':' ", arr[:])

print("Print out all items of array except last one: ", arr[:-1])

# ------------------ Searching for highest nubmer ------------------
# If we don't know index, we need to go through whole array sequentially

maxnum = arr[0]
for num in arr:
    if num > maxnum:
        maxnum = num
print(maxnum)

# ---------------------- TO BE CONTINUED... ------------------------
# ----------- LET ME KNOW IF YOU WANT TO ADD SOMETHING -------------
