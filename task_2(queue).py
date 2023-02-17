# -*- coding: utf-8 -*-
"""Task_2(Queue).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IRLX_1fgGii7rjbPKC5qaqAGpWK5ZcO6
"""

# Python program to create a LIFO queue.

import queue
insert = queue.LifoQueue(10)
insert.put(10)   #Add items in queue
insert.put(6)
insert.put(5)
insert.put(7)
insert.put(1)
insert.put(2)
insert.put(3)
insert.put(4)
insert.put(8)
insert.put(9)


de_queue = insert.get()  #Remove an item from queue
print('The item removed from the LIFO queue is ', de_queue)

def myfunc(n):
  return abs(n - 1)

thislist = [10,50,35,2,23,4,6,8,9,23,12,22,98,1]
thislist.sort(key = myfunc)
print(thislist)
thislist.insert(3, 5)
print(thislist)

# program which can take input of an integers list and sort it. Then can add any number in the list with sorted position 
try:
# Get input from user
  user_input = input("Enter each integer with whitespace: ").split()
  user_input = [int(i) for i in user_input]
# sorting
  user_input.sort()
  print("Sorted list:", user_input)

# Get a number from user
  num = int(input("Enter a number to add to the list: "))
  print("added number",num)

# Find the loc to add a num
  index = 0
  for i in range(len(user_input)):
      if num < user_input[i]:
          index = i
          break
      else:
          index = i + 1

# insert a num taken by user
  user_input.insert(index, num)


# Print the final sorted list 
  print("Sorted list with added number:", user_input)
except:
    print("Input is invalid")