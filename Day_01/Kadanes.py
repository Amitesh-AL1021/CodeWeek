def kadanes(arr):
    max_arr = arr[0]
    curr_arr = arr[0]
    for num in arr[1:]:
        curr_arr = max(num , curr_arr + num)
        max_arr = max(curr_arr ,max_arr)
    return max_arr
print(kadanes([12,3,49,596,4,594,594]))