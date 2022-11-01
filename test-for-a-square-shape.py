import os
import time
from math import pi
import numpy
from colorama import Fore, Back, Style
 

#x = symbols('x')
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)

#stackoveflow

p1 = numpy.array((3,4))
p2 = numpy.array((6,7))
p3 = numpy.array((9,4))
p4 = numpy.array((6,1))
p1p2 = numpy.linalg.norm(p1-p2)
p2p3 = numpy.linalg.norm(p2-p3)
p3p4 = numpy.linalg.norm(p3-p4)
p4p1 = numpy.linalg.norm(p4-p1)
p1p3 = numpy.linalg.norm(p1-p3)
p2p4 = numpy.linalg.norm(p2-p4)
#print("p1p2 =",p1p2)
#print("p2p3 =", p2p3)
#print("p1p3 =", p3p1)

if ((p1p2 ==  p2p3) and (p3p4 == p4p1) and (p1p3 == p2p4)):
    print(Back.WHITE, Fore.BLACK + 'the given shape is a square')
#print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
else:
    print("Not a square shape \n")



