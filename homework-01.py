"""

Name: David McGinn
Email: nicholasmcginn57@yahoo.com
Assignment:Homework 1 - Lists and Dictionaries
Due: 31 Jan 2016 @ classtime

"""


# 1.1 Basics

#A
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: (1,3)

a[4] = a[2] + a[-2]
Print(a)
# Prints: [1,5,4,2,6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: true

a[1] = [a[1], a[0]]
print(a)
# Prints: [1,(5,1),4,2,6]


#1.2 List Methods

#B
def remove_all(el, lst):
  """Removes all instances of el from lst. 
  Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
  Usage: remove_all(1, x)
  Would result in: [3, 2, 5, 7]
  """

  while el in lst:
    lst.remove(el)

#C
def add_this_many(x, y, lst):
  """ Adds y to the end of lst the number of times x occurs in lst. 
  Given: lst = [1, 2, 4, 2, 1]
  Usage: add_this_many(1, 5, lst)
  Results in: [1, 2, 4, 2, 1, 5, 5]
  """
  for i in range(x):
    lst.append(y)


#1.3 Slicing

#D
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3,1,4,2]

print(a)
# Prints: [3,1,4,2,5,3]

print(a[1::2])
# Prints: [1,2,3]

print(a[:])
# Prints: [3,1,4,2,5,3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1,4,2]

print(a[::-1])
# Prints: [3,5,2,4,1,3]


#1.4 For loops

#E
def reverse(lst):
  """ Reverses lst in place. 
  Given: x = [3, 2, 4, 5, 1] 
  Usage: reverse(x)
  Results: [1, 5, 4, 2, 3]
  """
  tmp = 0
  for i in range(len(lst)//2):
    tmp = lst[i]
    lst[i] = lst[-1-i]
    lst[-1-i] = tmp

#F
def rotate(lst, k):
  """ Return a new list, with the same elements of lst, rotated to the right k.
  Given: x = [1, 2, 3, 4, 5]
  Usage: rotate(x, 3)
  Results: [3, 4, 5, 1, 2]
  """
  return lst[-k:] + lst[:-k]


#2.0 Dictionaries

#H
print('colin kaepernick' in superbowls)
#Prints: false

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: false

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {('eli manning','giants'): 2 'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {('eli manning','giants'): 2 'peyton manning': 1, 'tom brady': 3, 'cat',  'joe flacco': 1, 'joe montana': 4}


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {('eli manning','giants'): 5 'peyton manning': 1, 'tom brady': 3, 'cat',  'joe flacco': 1, 'joe montana': 4}

superbowls[('steelers', '49ers')] = 11
print(superbowls)
#Prints: {('steelers','49ers'): 11, ('eli manning','giants'): 5 'peyton manning': 1, 'tom brady': 3, 'cat',  'joe flacco': 1, 'joe montana': 4}

#I
def replace_all(d, x, y):
  """Replaces all values of x with y. 
  Given: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}} 
  Usage: replace_all(d,3,1)
  Results: {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}} 
  """
  for k in d.keys():
    if isinstance(d[k],dict):
      replace_all(d[k], x, y)
    elif d[k] == x:
      d[k] = y

      
#J
def rm(d, x):
  """Removes all pairs with value x. 
  Given:  d = {1:2, 2:3, 3:2, 4:3}
  Usage:  rm(d,2)
  Results: {2:3, 4:3}
  """
  remove = [k for k, v in d.items() if v == x]
  for k in remove:
    del d[k]