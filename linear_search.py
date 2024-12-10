def linear_search(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i

arr = [40, 30, 50, 10, 20]
key = int(input("Enter key: "))

result = linear_search(arr, key)

if key not in arr:
    print("Key not Found..!")
else:
    print(f"{key} found at location {result+1}")