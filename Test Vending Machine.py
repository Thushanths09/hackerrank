#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine():
    def __init__(self,variable1,variable2):
        self.variable1=variable1
        self.variable2=variable2

    def buy(self,x,y):
        if(self.variable1>=x and x*self.variable2<=y):
            self.variable1-=x
            return y-(x*self.variable2)
        else:
            if(self.variable1<x):
                return "Not enough items in the machine"
            else:
                return "Not enough coins"
            
            
         
        
    pass