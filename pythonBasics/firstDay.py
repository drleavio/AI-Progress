#------------------------------------------basics of python----------------------------------------------------
import sys

print(sys.version)
print("hello world")

x=10
y=20

def add(x,y):
    print(x+y)

add(x,y)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



x = "awesome"

def myfunc():
  global  x 
  x = "fantastic"
 

myfunc()

print("Python is " + x)

import random

x=random.randrange(1,10)
print(x)

x="banana"

for y in x:
    print(y)

price = 59
txt = f"The price is {price} dollars"
print(txt)

#---------------------------------------------lists in python----------------------------------------------------------

mylist = ["apple", "banana", "cherry"]

# To determine how many items a list has, use the len() function:
print(len(mylist))

# List items are indexed and you can access them by referring to the index number:
print(mylist[1])

# Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.
print(mylist[-1])

# You can specify a range of indexes by specifying where to start and where to end the range.
print(mylist[1:2])

# To determine if a specified item is present in a list use the in keyword:
if("apple" in mylist):
    print("Apple is present")

# To change the value of a specific item, refer to the index number:
mylist[1]="mango"

# The insert() method inserts an item at the specified index:
mylist.insert(1,"grapes")

# To add an item to the end of the list, use the append() method:
mylist.append("pineapple")

# To append elements from another list to the current list, use the extend() method.
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thistuple = ("kiwi", "orange")
mylist.append(thistuple)

# The remove() method removes the specified item.
mylist.remove("grapes")

# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.
mylist.pop(1)

# The clear() method empties the list.
mylist.clear()

# You can loop through the list items by using a for loop:
for x in mylist:
    print(x)

# You can also loop through the list items by referring to their index number.
for i in range(len(mylist)):
    print(mylist[i])

# You can loop through the list items by using a while loop.
i=0
while(i<len(mylist)):
    print(mylist[i])
    i=i+1

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
mylist.sort()

# To sort descending, use the keyword argument reverse = True:
mylist.sort(reverse=True)

# You can also customize your own function by using the keyword argument key = function.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# The reverse() method reverses the current sorting order of the elements.
mylist.reverse()

# You can use the built-in List method copy() to copy a list.
newList=mylist.copy()

# Python has a set of built-in methods that you can use on lists.
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



#------------------------------------------------tuples in python----------------------------------------------------

x=tuple(("apple","mango","banana"))
y=tuple(x)
print(type(x))
print(type(y))
print(x)
print(y)