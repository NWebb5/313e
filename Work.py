#  File: Work.py

#  Description: This program calculates the minimum number of lines of code the user writes before
#  having to drink a cup of coffee to write n lines before going to bed. 
#  We use linear and binary searches to find this number.

#  Student Name: Nicholas Webb

#  Student UT EID: nw6887

#  Partner Name: EJ Porras

#  Partner UT EID: ejp2488

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 2/28/2022

#  Date Last Modified: 3/2/2022

import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  total = 0
  i = 0
  term = v
  while term > 0:
    term = v//(k**i)
    total += term
    i+=1
  return total

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  for i in range(1,n+1):
    if sum_series(i,k) >= n:
      return i
  return 0
    
  
# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  beg = 1
  end = n
  while (beg <= end):
    mid = (end+beg)//2
    if sum_series(mid, k) >=n and sum_series(mid-1, k) < n:
      return mid
    elif(sum_series(mid, k) >= n):
      end = mid - 1
    else:
      beg = mid + 1
  return 0
    

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
