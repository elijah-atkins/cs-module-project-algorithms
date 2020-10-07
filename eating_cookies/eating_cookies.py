'''
Input: an integer
Returns: an integer
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

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 30

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
