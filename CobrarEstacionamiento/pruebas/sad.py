'''
Created on 11/2/2015

@author: Tony
'''
import unittest
from calcularCosto import *

class Test(unittest.TestCase):


    def testName(self):
        h1,h2 = calcularEstadia(datetime.datetime(4,4,4,7,50), datetime.datetime(4,4,4,14,55)) 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()