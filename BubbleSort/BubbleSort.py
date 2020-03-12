# Bubble Sort
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)
    return arr

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

# Driven Program 
if __name__ == "__main__":
    array = [2,5,6,1,4,7,9,3]
    print("Unsorted Array: ", array)
    print(bubbleSort(array))
