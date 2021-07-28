"""
Created on Wed Jul 28 13:33:02 2021

@author: Yasin BİRCAN
"""

import math

key = 1

def checkDegreeValue(r_radian):
    try:
        r_radian = int(r_radian)
        r_radian_check = 0

    except:
        try:
            r_radian = float(r_radian)
            r_radian_check = 0
        except:
            print("Please enter integer value only. Not string value.")
            r_radian_check = 1
    return r_radian_check

def calculateRadianValue(r_radian):
    degree_value = float(r_radian)*(180/math.pi)
    return degree_value

while key == 1:
    radian = input("Please Enter The Radian Value: ")
    key = checkDegreeValue(radian)
degree = calculateRadianValue(radian)
print("Radian Value: " + str(radian))
print("Degree Value: " + str(degree))