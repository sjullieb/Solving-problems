#!/bin/python

from __future__ import print_function

import os
import sys

class Node:
    def __init__(self, value = []):
        self.value = value
        self.next = None
        
class DynamicArray:
    
    def __init__(self, length):
        self.length = length
        self.first_el = Node()
        self.last_el = self.first_el
        self.current_index_in_one_arr = 0
        
    def AddElement(self, data):
        
        if self.current_index_in_one_arr == self.length:
            print(self.length)
            print(self.first_el.value)
            new_el = Node() 
            #new_el.value = [](length)
            #new_el.next = null

            self.last_el.next = new_el
            self.last_el = new_el
            self.current_index_in_one_arr = 0	

        self.last_el.value.append(data)
        print(self.last_el.value)
        self.current_index_in_one_arr += 1
    
    def FindElement(self, index):
        num_array = int(index / self.length)
        actual_index = index % self.length

        arr_el = self.first_el
        for i in range(1, num_arr+1):
            if self.arr_el.next == None:
                exception
            arr_el = arr_el.next 

        return arr_el.value[actual_index]
    
    def PrintArrays(self):
        tmp = self.first_el
        print(self.first_el)
        while True:
            print(tmp.value)
            print(tmp.next)
            if tmp.next == None:
                break
            else: 
                tmp = tmp.next
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = DynamicArray(2)
    arr.AddElement(2)
    arr.AddElement(4)
    arr.PrintArrays()
    print('addin 2 more elements')
    arr.AddElement(3)
    arr.PrintArrays()
    arr.AddElement(9)
    arr.PrintArrays()
    
    fptr.close()
