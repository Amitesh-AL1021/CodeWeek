def rotateArray(arr,k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
print(rotateArray([1,2,3,4,5,6,75,4,53,53],3))