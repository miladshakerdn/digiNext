def minSwaps(arr):
    swaps = 0;
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            swaps += 1
    return swaps

print(minSwaps([7, 1, 3, 2, 4, 5, 6]))