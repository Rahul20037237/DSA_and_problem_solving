import time
def binary_search(low,high,target,arr):
    mid=(low+high)//2
    if target==arr[mid]:
        print(arr[mid],mid,low,high)
    elif arr[mid]>target:
       binary_search(low,mid-1,target,arr)
    else:
        binary_search(mid+1,high,target,arr)
arr=[2,4,5,6,7,8,9,12,14,17,19,22,25,27,28,33,37]
binary_search(0,len(arr),22,arr)