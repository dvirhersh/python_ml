# get list of items
# buble sort the list:
    # iterate on all indexes
    # if adjacent items are out of order - swap them
    # repeat n times (n is len of the list)

arr = [5,7,3,7,3,7,9,2,1]

for j in range(len(arr) - 1):
    for i in range(len(arr)-1 - j):
        if arr[i + 1] < arr[i]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)