'''
Input: an integer
Returns: an integer
'''
'''
def eating_cookies(n):
    # Your code here
    #if there are less than zero cookies return 0
    if (n < 0):
        return 0
    #return 1 to end recusion when 
    elif (n==1 or n==0):
        return 1
    else:
        return (eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
'''
def cookie_tracker(arr):
    next_value = sum(arr)
    return arr[1:] + [next_value]

def eating_cookies(n, cache=None):
    tracker = [0,0,1]
    while n > 1:
        tracker = cookie_tracker(tracker)
        n -= 1
    return sum(tracker)
import sys
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = int(sys.argv[1])

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
