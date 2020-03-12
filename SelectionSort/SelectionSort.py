# Selection Sort
def selectionSort(array):
    for i in range(len(array)):
        index = i
        for j in range(i+1, len(array)):
            if array[j] < array[index]:         # Ascending Order
                index = j                       # Find smallest element
        if index != i: swap(array, index, i)    # Swap with left most element
    return array

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


# ---------------- Testing --------------------
if __name__ == '__main__':
    array = [9,6,69,10,100,96,26,4]
    print("Unsorted array: ", array)
    print(selectionSort(array))