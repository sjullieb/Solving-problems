#!/bin/python

from __future__ import print_function

import os
import sys

class Stack:
    
    def __init__(self):
        self.arr = []
        self.count = 0
        
    def push(self, element):
        self.arr.append(element)
        self.count += 1
        
    def pop(self):
        if self.count > 0:
            self.count -= 1
            return self.arr.pop()
        else:
            Exception
            
    def printstack(self):
        print(self.arr)  
        
    def peak(self):
        print(self.arr[self.count - 1])

    def NumberOfElements(self):
        return self.count
        

def Hanoy(n, st_from, st_temp, st_to):
	 
	if n <= 0: return
	
	Hanoy(n - 1, st_from, st_to, st_temp)
	st_to.push(st_from.pop())
	Hanoy(n - 1, st_temp, st_from, st_to)	
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar = map(int, raw_input().rstrip().split())
        
    st1 = Stack()
    for el in ar:
        st1.push(el)

    st2 = Stack()
    st3 = Stack()
    print('before')
    st1.printstack()
    st2.printstack()
    st3.printstack()
    
    Hanoy(st1.NumberOfElements(), st1, st2, st3) 
    print('after')
    st1.printstack()
    st2.printstack()
    st3.printstack()
    
    fptr.close()
