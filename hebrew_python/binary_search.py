# get list and item to search
# if list is empty - return False
# if middle of list is item - return True
# if middle is bigger than item - perform search for left of list
# if middle is smaller than item - perform search for right of list

# def binary_search(arr, item):
#     # if len(arr) == 0:
#     if not arr:
#         return False
#     i = len(arr) // 2
#     if arr[i] == item:
#         return True
    
#     if arr[i] > item:
#         return binary_search(arr[:i], item)
#     if arr[i] < item:
#         return binary_search(arr[i+1:], item)

def binary_search(arr, item):
    i = 0
    j = len(arr) - 1 
    while i<=j:
        mid = (i+j)//2
        if item < arr[mid]:
            j = mid - 1
        elif item > arr[mid]:
            i = mid + 1
        elif arr[mid] == item:
            return True
    return False

arr = [1,3,5,6,7,10,19,25,36]
print(binary_search(arr, 6))
print(binary_search(arr, 2))
print(binary_search([], 2))
    