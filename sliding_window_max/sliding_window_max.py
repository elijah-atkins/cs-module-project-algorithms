'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def return_greatest(arr):
#     result = arr[0]
#     for x in arr:
#         if x > result:
#             result = x
#     return result

# def sliding_window_max(nums, k):
#     # Your code here
#     result = []
#     i = 0
#     while i <= len(nums) - k:
#         result.extend([max(nums[i:i+k])])
#         i += 1
#     return result

#solution using queue
from collections import deque

def sliding_window_max(nums, k):
    results = []
    q = deque()
    
    for i, n in enumerate(nums):
        while len(q) > 0 and n > q[-1]: 
            q.pop()
        q.append(n)
        window_range = i - k + 1

        #as long as our windows range is == k we will add elements to our queue
        if window_range >= 0:
             #add the max elem(in this case 1st in the queue)
             results.append(q[0])
             if nums[window_range] == q[0]:
                 q.popleft()
    return results    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
