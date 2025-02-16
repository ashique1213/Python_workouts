def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while high >= 1:
        mid = (low+high)//2

        if arr[mid]==target:
            print("target:",mid)
            return
        if target>arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return print("not found")

arr = [1,2,3,4,5,6,7,8,9,10]
binary_search(arr,6)