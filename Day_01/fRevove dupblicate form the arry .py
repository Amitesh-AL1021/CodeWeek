def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

print(find_duplicates([23,4,3,4,33,43,23,4,5,3,2,10]))