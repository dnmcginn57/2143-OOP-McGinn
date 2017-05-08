# I AM STILL WORKING ON THIS PLEASE DON'T GRADE IT YET

### Question 1
```python
def dirReduc(list):
    """
    @Method: dirReduc
    @Description:
        Accepts a list of cardinal directions and removes
        directions that cancel eachother out
    @Returns: A simplified list of directions
    """

    #A dictionary to hold each cardinal direction and the ammount of times
    #   it is in the list
    d = {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0}
    L = []

    #changes the key to the number of occurences
    d["NORTH"] = list.count("NORTH")
    d["SOUTH"] = list.count("SOUTH")
    d["EAST"] = list.count("EAST")
    d["WEST"] = list.count("WEST")

    #Simplifys North and South
    if d["NORTH"] > d["SOUTH"]:
        d["NORTH"] = d["NORTH"] - d["SOUTH"]
        del d["SOUTH"]
    elif d["NORTH"] == d["SOUTH"]:
        del d["NORTH"]
        del d["SOUTH"]
    else:
        d["SOUTH"] = d["SOUTH"] - d["NORTH"]
        del d["NORTH"]

    #Simplifys East and West
    if d["EAST"] > d["WEST"]:
        d["EAST"] = d["EAST"] - d["WEST"]
        del d["WEST"]
    elif d["EAST"] == d["WEST"]:
        del d["EAST"]
        del d["WEST"]
    else:
        d["WEST"] = d["WEST"] - d["EAST"]
        del d["EAST"]

    #Puts anything left in the dictionary into the new list
    for i in d:
        L.append(i)

    return L
    
```
### Question 2
```python
def ChangeMaker(L):
    """
    @Method: ChangeMaker
    @Description:
        Accepts a list of intergers which may be 100, 50, or 25
        in any order
    @Returns: "YES" if cashier can give everyone in line change "NO" otherwise
    """

    #tracks the bills in the drawer
    drawer = []

    for i in L:

        #if the customer has exact change it is added to the drawer
        if i == 25:
            drawer.append(i)

        #if the customer pays with a 50
            #check to see if there is a 25 in the drawer to make change with
            #if there is the 25 is changed for the 50
        elif i == 50:
            if drawer.count(25) == 0:
                return "NO"
            else:
                drawer.remove(25)
                drawer.append(50)

        #if the customer pays with a 100
            #check to see if there is at least one 50 and one 25 or 3 25's
            #if there is they are changed for the 100
        elif i == 100:
            if drawer.count(50) == 0 and drawer.count(25) < 3:
                return "NO"
            elif drawer.count(50) > 0 and drawer.count(25) == 0:
                return "NO"
            else:
                if drawer.count(50) > 0:
                    drawer.append(i)
                    drawer.remove(50)
                    drawer.remove(25)
                else:
                    drawer.append(i)
                    drawer.remove(25)
                    drawer.remove(25)
                    drawer.remove(25)

    #finally if all tests are passed the method returns "YES"
    return "YES"
```
### Question 3
```python
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[%d,%d]" % (self.x, self.y)

class Shape(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        pass

class Square(Shape):
    def __init__(self, s1, p1 = None, p2 = None):
        super().__init__(p1, p2)
        self.s1 = s1

    def perimeter(self):
        return self.s1*4

    def area(self):
        return self.s1**2

class Rectangle(Shape):
    def __init__(self, s1, s2, p1 = None, p2 = None):
        super().__init__(p1, p2)
        self.s1 = s1
        self.s2 = s2

    def area(self):
        return self.s1 * self.s2

class Cube(Square):
    def __init__(self, s1):
        super().__init__(s1)

    def area(self):
        return self.s1**3

    def surfaceArea(self):
        face = super().area()
        return face*6
```
### Question 4
```python
def dupLetters(s):
    """
    @Method: dupLetters
    @Description:
      Method accepts a string of letters
      This method is not case sensitive
    @Returns: the number of letters which are repeated
      NOT THE NUMBER OF TIMES THEY ARE REPEATED
    """

    s = s.lower()
    repeats = 0


    for i in s:
        if s.count(i) > 1:
            repeats += 1
            s = s.replace(i, "")

    return repeats
  
```
### Question 5
```python
def consecutive(L):
    """
    @Method: consecutive
    @Description:
        Locates the first value in the array which is not consecutive
    @Returns: the first inconsecutive value or none if there isn't one
    """

    for i in range(len(L) - 1):
        #the check is not preformed for the first value
        if i != 0:
            if L[i] != L[i - 1] and L[i] != L[i-1] + 1:
                return L[i]

    return None
```
### Question 6
```python
class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return '%s %s' % (self.firstname, self.lastname)


class Parent(Person):
    """
    @Class: Parent
    @Methods:
        __init__: accepts a first and last name and initilizes an empty list to hold
            its children
        birth: accepts a child and adds it to the list of children
    """
    def __init__(self, first, last):
        super().__init__(first, last)
        self.children = []

    def birth(self, child):
        self.children.append(child)

class Child(Person):
    """
    @Class: Child, inherits person
    @Methods:
        __init__: accepts a first and last name as well as a parent
    """

    def __init__(self, first, last, parent):
        super().__init__(first, last)
        self.parent = parent
```
### Question 7
