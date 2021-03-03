#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:31:33 2021

@author: basakulcay
"""

from array import array

period = [1, 0, 1]
segment = [[21, 46, 92, 130, 180],
           [12, 59, 15, 18, 34],
           [9, 21, 37, 50, 61]]
alpha = [[0.7, 0.4, 0.75, 0.713, 0], 
         [0.73, 0.691, 0.654, 0.616, 0], 
         [0.78, 0.745, 0.71, 0.675, 0]]

U=40
A=0
I=0

segmentCount=0
for segmentElement in segment:
    segmentCount += len(segmentElement)/len(segment)



for i in range(len(period)):
    for j in range(int(segmentCount)):
        if U>=segment[i][j]:
            A=+((U-segment[i][j])*alpha[i][j])+segment[i][j]
            I+=U-A
            for k in range(1,len(period)):
                print(segment[k][j])
                while I<=segment[k][j]:
                    print('Not viable')
                    U+=1
                    I+=1-alpha[i][j]
                    print('Increased U',U)
                    print('New inventory',I)
                
            print(A)
            print('Inventory is',I)
        

