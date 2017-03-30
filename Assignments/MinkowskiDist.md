David McGinn
3-29-17
2143 - OOP

from http://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/

###Minkowski Distance

####Python Implementation
```python
from math import*
from decimal import Decimal

def nth_root(value, n_root):

    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

def minkowski_distance(x,y,p_value):

    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

print minkowski_distance([0,3,4,5],[7,6,3,-1],3)
```

####Outputs
```python
8.373
[Finished in 0.0s]
```

could be modified for use for the flow game by taking into account both
taxi-cab distance and Euclidean distance
