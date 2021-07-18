"""
Created on Sun Jul 18 15:18:30 2021

@author: Yasin BİRCAN
"""

import math

key = 1

def checkDegreeValue(r_degree):
    try:
        r_degree = int(r_degree)
        r_degree_check = 0

    except:
        try:
            r_degree = float(r_degree)
            print("Please enter integer value only. Not float value.")
            r_degree_check = 1
        except:
            print("Please enter integer value only. Not string value.")
            r_degree_check = 1
    return r_degree_check

def calculateRadianValue(r_degree):
    radian_value = float(r_degree)*(math.pi/180)
    return radian_value

while key == 1:
    degree = input("Lütfen Derece Değerini Giriniz: ")
    key = checkDegreeValue(degree)
radian = calculateRadianValue(degree)
print("Degree Value: " + str(degree))
print("Radian Value: " + str(radian))