'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeros = 0
    result = []
    for digit in arr:
        #count all zeros found
        if digit == 0:
            zeros += 1
        #add non zero values to result array
        else:
            result.append(digit)
    #return result array plus an array with the number of zeros found
    return result + [0] * zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")