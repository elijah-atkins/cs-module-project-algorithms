#!/usr/bin/python

import sys


'''
def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  if n == 1:
    return options
  output = []
  listA = rock_paper_scissors(n -1)

  for subList in listA:
    for play in options:
      newPlay = subList + play
      output.append(newPlay)
  return output
'''

def rock_paper_scissors(n):
  options = [["rock"],["paper"],["scissors"]]
  output = []
  #base case return array with empty array 
  if n == 0:
    return [[]]
  #return default set of possible plays
  if n == 1:
    return options
  #populate listA with solution of n-1
  listA = rock_paper_scissors(n-1)

  #append all three options to every sublist in ListA
  for subList in listA:
    output.append(subList + options[0])
    output.append(subList + options[1])
    output.append(subList + options[2])
  return output

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')