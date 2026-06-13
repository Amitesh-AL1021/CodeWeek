def twosum(arr,target):
    dict = {}
    for i in range(len(arr)):
        need = target - arr[i]
        if need in dict:
            return [dict[need],i]
        dict[arr[i]] = i
print(twosum([2,3,4,5,7,2] , 9))

