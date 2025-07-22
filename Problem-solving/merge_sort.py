def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    print("To be merged !!")
    print(left, right)
    result = []
    i = j = 0

    # Merge both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    print("merged")
    print(result)
    return result

# Example usage
nums = [5, 2, 4, 1, 3]
print(nums)
sorted_nums = merge_sort(nums)
print(sorted_nums)  # Output: [1, 2, 3, 4, 5]