def linearSearch( arr, x):
    n = len(arr)
    for i in range(0,n):
        if (arr[i] == x):
            return i
    return -1
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    x = 6
    result = linearSearch(arr, x)
    if(result == -1):
        print("Element not found in array")
    else:
        print("Element found at index: ", result)
    
