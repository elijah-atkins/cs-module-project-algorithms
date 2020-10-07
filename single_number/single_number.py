'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
solution with bitwise operators
https://wiki.python.org/moin/BitwiseOperators
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