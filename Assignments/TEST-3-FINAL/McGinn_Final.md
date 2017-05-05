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
### Question 4
### Question 5
### Question 6
### Question 7
