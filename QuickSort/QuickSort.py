# Quick Sort Algorithm
def quickSort(array, low, high):
    if low >= high: return
    pivot = partition(array, low, high)
    quickSort(array, low, pivot-1)
    quickSort(array, pivot+1, high)
    return

def partition(array, low, high):
    pivotIndex = (low+high) // 2
    swap(array, pivotIndex, high)

    # Ascending Order
    i = low
    for j in range(low, high):
        if array[j] <= array[high]:
            swap(array, i,j)
            i += 1
    swap(array, i, high)
    return i

def swap(arr, x,y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

# Driven Program
if __name__ == '__main__':
    array = [9,69,6,10,96,3,5]
    print("Unsorted array: ", array)
    quickSort(array, 0, len(array)-1)
    print(array)