"""
Jack Sanders
CIS 313, Intermediate Data Structures
11/18/2019


GCD & LCM in Python 3
"""

import math


class mathOps:
    def __init__(self, u, v):
        self.u = u
        self.v = v
    
    def __repr__(self):
        return "LeastCommonMultiple({}, {})".format(self.u, self.v)
    
    def __str__(self):
        return "GreatestCommonDivisor({}, {}).".format(self.u, self.v)

    def valid(self):
        return isinstance(self.u, int) and isinstance(self.v, int)
    
    def gcd(self):
        # Find the greatest common divisor of a and b
        # Hint: Use Euclid's Algorithm
        # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure

        tempU = self.u
        tempV = self.v
         
        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError
            if isinstance(tempU, str) or isinstance(tempV, str):
                raise TypeError                 # if one more string inputs --> TypeError

            tempU = abs(math.ceil(tempU))       # accounts for float and/or negative inputs
            tempV = abs(math.ceil(tempV))       # accounts for float and/or negative inputs
            while tempV != 0:                   # if tempV == 0, return tempU
                tempZ = tempV                   # set a new variable (tempZ) to tempV so I can manipulate tempV
                tempV = tempU % tempV           # set tempV equal to the remainder of tempU / tempV
                tempU = tempZ                   # set tempU  = tempZ
            return tempU                        # accounts for negative inputs

        except TypeError:
            print("One or both the types of", tempU, " and ", tempV, "are strings")
            raise TypeError
        except OverflowError:
            print("One or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise OverflowError

    def lcm(self):
        # Find the least common multiple of a and b
        # Hint: Use the gcd of a and b
        tempU = self.u
        tempV = self.v
        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError
            if tempU == 0 or tempV == 0:
                raise ZeroDivisionError             # if one or both inputs == 0 --> undefined.

            tempU = abs(math.ceil(tempU))           # accounts for float and/or negative inputs
            tempV = abs(math.ceil(tempV))           # accounts for float and/or negative inputs
            return (tempU * tempV) / self.gcd()

        except ZeroDivisionError:
            print("One or both the values of", tempU, " and ", tempV, "are equal to zero")
            raise ZeroDivisionError
        except OverflowError:
            print("One or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise OverflowError
