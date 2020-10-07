'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def return_greatest(arr):
    result = arr[0]
    for x in arr:
        if x > result:
            result = x
    return result

def sliding_window_max(nums, k):
    # Your code here
    result = []
    array_length = len(nums)
    i = 0
    while i <= array_length - k:
        result.append(return_greatest(nums[i:i+k]))
        i += 1
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
