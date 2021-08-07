# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 07:39:08 2021

@author: pc2
"""
import math

key = 1
key2 = 1

def checkInputValue(r_value):
    try:
        r_value = int(r_value)
        r_value_check = 0

    except:
        try:
            r_value = float(r_value)
            r_value_check = 0
        except:
            print("Please enter integer value only. Not string value.")
            r_value_check = 1
    return r_value_check

def calculateCylinderArea(r_radius, r_height):
    cylinder_area = 2*math.pi*float(r_radius)*(float(r_radius)+float(r_height))
    return cylinder_area

def calculateCylinderVolume(r_radius,r_height):
    cylinder_volume = math.pi*float(r_radius)**2*float(r_height)
    return cylinder_volume

while key == 1:
    radius = input("Please Enter The Radius of the Cylinder: ")
    key = checkInputValue(radius)
while key2 == 1:
    height = input("Please Enter The Height of the Cylinder: ")
    key2 = checkInputValue(height)

cylinder_area_value = calculateCylinderArea(radius,height)
cylinder_volume_value = calculateCylinderVolume(radius,height)
print("Surface Area of Cylinder " + str(cylinder_area_value))
print("Volume of Cylinder: " + str(cylinder_volume_value))