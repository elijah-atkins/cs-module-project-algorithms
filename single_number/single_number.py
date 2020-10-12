'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
solution with bitwise operators
https://wiki.python.org/moin/BitwiseOperators
XOR is a binary operation, it stands for "exclusive or", 
that is to say the resulting bit evaluates to one if only 
exactly one of the bits is set.

This is its function table:

a | b | a ^ b
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0
'''
def single_number(arr):
    # Your code here
    answer = 0
    for i in arr:
        #flip bit for each item in array
        #items with duplicates get canceled out 
        #leaving only the single number
        answer ^= i
    return answer


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")