"""
Created on Wed Aug 25 2021

@author: Yasin BİRCAN
"""
key=1
key2=1
key3 = 1
import math

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

print("Quadratic Equation: ax^2+bx+c")
while key == 1:
    coefficient_a = input("Please enter 'a' coefficient: ")
    key = checkInputValue(coefficient_a)
coefficient_a = float(coefficient_a)
while key2 == 1:
    coefficient_b = input("Please enter 'b' coefficient: ")
    key2 = checkInputValue(coefficient_b)
coefficient_b = float(coefficient_b)
while key3 == 1:
    coefficient_c = input("Please enter 'c' coefficient: ")
    key3 = checkInputValue(coefficient_c)
coefficient_c = float(coefficient_c)
delta = (coefficient_b**2) - (4*coefficient_a*coefficient_c)
if delta > 0 or delta == 0:
    root_1 = (-coefficient_b + math.sqrt(delta))/(2*coefficient_a)
    root_2 = (-coefficient_b - math.sqrt(delta))/(2*coefficient_a)
    print("First Root: " + str(root_1) + " Second Root: " + str(root_2))
elif delta < 0:
    print("The equation has no roots.")