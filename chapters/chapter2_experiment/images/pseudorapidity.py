import numpy as np
import math

def pseudorapidity(theta):
    return(-np.log(np.tan(float(theta)/2)))

l1 = pseudorapidity(math.degrees(89))
print(l1)
