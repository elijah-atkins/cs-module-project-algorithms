#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here
  #create array with number of options for each amount
  #There is only one way to give change for zero dollars
  #There is exaclty one way to give change in pennies to every amount over zero
  #There are no new ways to give change until the amount >= than any denomination
  #once 
  cache = [1] + [0] * amount
  for coin in denominations:
    for i in range(coin, amount+1):
      cache[i] += cache[i-coin]
  return(cache[amount])



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")