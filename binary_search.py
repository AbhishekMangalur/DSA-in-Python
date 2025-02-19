def binary_search(arr, key):
    low = 0
    high = len(arr)
    
    while low <= high:
        mid = (low + high) // 2
        
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

arr = [10, 20, 30, 40, 50]
key = int(input("Enter key: "))

result = binary_search(arr, key)

if key not in arr:
    print("Key not found..!")
else:
    print(f"{key} found at location {result + 1}")