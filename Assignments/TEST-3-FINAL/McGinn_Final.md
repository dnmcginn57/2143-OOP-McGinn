+ David McGinn
+ 2143-OOP
+ due: 5-10-17

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
    """
    @Class: Square inherits Shape
    @Methods:
        __init__: accepts a side length, may also accept two points
        perimeter: returns the perimeter of the square
        area: overrides Shape's area, squares the sides
    """
    def __init__(self, s1, p1 = None, p2 = None):
        super().__init__(p1, p2)
        self.s1 = s1

    def perimeter(self):
        return self.s1*4

    def area(self):
        return self.s1**2

class Rectangle(Shape):
    """
    @Class: Rectangle inherit's Shape
    @Methods:
        __init__: accepts 2 side lengths and two points optionally
        area: Overrides Shape's area, multiplies the two sides together
    """
    def __init__(self, s1, s2, p1 = None, p2 = None):
        super().__init__(p1, p2)
        self.s1 = s1
        self.s2 = s2

    def area(self):
        return self.s1 * self.s2

class Cube(Square):
    """
    @Class: Cube inherits Square
    @Methods:
        __init__: accepts one side length
        area: Overrides Square's area, sides are cubed, so really it returns the volume
            of the cube
        surfaceArea: multiplies parent's area by 6 
    """
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
```python
import random

class Wheel(object):
    """
    @Class: Wheel
    @Description:
        Represents a roulette wheel
    @Methods:
        spin
    """

    def __init__(self):
        """
        @Method: __init__
        @Description:
            sets up the wheel, accepts no parameters. populates a list for each color
            the value 37 represents 00 since 00 is just 0 but we need 2 distinct values that mean 0
        """
        self.green = [0, 37]
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black = []
        for i in range(36):
            if not i in self.red:
                self.black.append(i)
        self.black.pop(0)

    def spin(self):
        """
        @Method: spin
        @Description:
            Accepts no parameters, determines where the ball lands after
            a spin
        @Returns: a dictionary representing the ball's location
        """
        land = random.randint(1, 37)
        d = {}
        if land in self.red:
            d['number'] = land
            d['color'] = 'red'
        elif land in self.black:
            d['number'] = land
            d['color'] = 'black'
        else:
            #the chance of landing on green isn't changed but 00 is the same as 0
            if land == 37:
                land = 0
                d['number'] = land
                d['color'] = 'green'
        return d

class Table(object):
    """
    @Class: Table
    @Description: Represents a roulette table
    @Methods:
        checkAdj
        getPayout
    """
    def __init__(self):
        """
        @Method: __init__
        @Description:
            would initialize with a dictionary holding every type of bet and its payout
            as a factor by which to multiply the player's bet
        """
        #for example,
        self.bets = {'Even': 2, 'Single': 35}
        #and so on

    def checkAdj(self, n):
        """
        @Method: checkAdj
        @Description:
            This method would accept a list of numbers
            it would then check to see if the numbers in that
            list would be adjacent on a roulette table
            a list is used since a player can bet on anywhere from
            2 to 4 numbers that are adjacent
        @Returns:
            True if numbers are adjacent
            False if they are not
        """
        pass

    def getPayout(self, btype):
        """
        @Method: getPayout
        @Description:
            accepts as a string a type of bet.
            searches the bets dictionary for that type of bet
        @Returns:
            the factor by which to multiply the winning player's money
        """
        pass

class Player():
    """
    @Class: Player
    @Description: Represents a player of roulette
    @Methods:
        placeBet
        payout
    """
    def __init__(self, name, bank):
        self.name = name
        self.total_bank = bank
        self.current_bet_amount = 0
        self.current_bet = None

    def placeBet(self, amt, bet):
        """
        @Method: placeBet
        @Description:
            This accepts an amount of money and a bet.
            the amount of money is subtracted from the player's bank
            and current_bet_amount is set to this amount.
            current_bet is set to what the player places a bet on
        @Returns: this method returns nothing probably
        """
        pass

    def payout(self, winnings):
        """
        @Method: payout
        @Description:
            in the event the player wins the bet, their winnings(calculated externally)
            are added to their total bank
        """
        pass

class Game(object):
    """
    @Class: Game
    @Description:
        contains all objects for a roulette game
        and manages said game
    @Methods:
        playGame
    """
    def __init__(self, players):
        """
        @Method: __init__
        @Description:
            accepts a list of players
            initializes a table object and a wheel object
        """
        self.players = players
        self.table = Table()
        self.wheel = Wheel()

    def playGame(self):
        """
        @Method: playGame
        @Description:
            This method is responsible for running the game
            keeps track of players, their bets, and bet ammounts
            responsible for checking if anyone won and pays them the
            appropriate ammount if they did
        """
        #everyone places a bet
        result = self.wheel.spin()
        #check if anyone wins
        #pays winners

    def bustOut(self, p):
        """
        @Method: BustOut
        @Description:
            this method would remove a player from the game
            when said player runs out of money
        """
        self.players.remove(p)

```
