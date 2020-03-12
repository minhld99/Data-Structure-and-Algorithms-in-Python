# Insertion Sort
def insertionSort(array):
    for i in range(len(array)):
        j = i
        while (j>0 and array[j-1] > array[j]):
            swap(array, j, j-1)
            j = j-1
    return array

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

# Driven Program
if __name__ == '__main__':
    array = [7,2,1,6,69,9,3]
    print("Unsorted array: ", array)
    print(insertionSort(array))