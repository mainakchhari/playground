
def insertionSort(arr):
    # O(N^2)
    n = len(arr)
    for j in range(2,n):
        key = arr[j]
        i=j-1
        while arr[i] > key and i>=0:
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key
        print(arr)
    return arr

if __name__ == "__main__":
    data = [2, 3, 4, 5, 6, 7, 8, 1, 9, 0]
    data = insertionSort(data)
    print(data)