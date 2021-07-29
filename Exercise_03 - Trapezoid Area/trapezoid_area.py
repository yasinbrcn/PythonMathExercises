"""
Created on Thu Jul 29 07:51:26 2021

@author: Yasin BİRCAN
"""
key = 1
key2 = 1
key3 = 1

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

def calculateTrapezoidArea(r_base1_value, r_base2_value, r_height):
    trapezoid_area = ((float(r_base1_value)+float(r_base2_value))/2)*float(r_height)
    return trapezoid_area

while key == 1:
    base1_value = input("Please Enter The First Base Value: ")
    key = checkInputValue(base1_value)
while key2 == 1:
    base2_value = input("Please Enter The Second Base Value: ")
    key2 = checkInputValue(base2_value)
while key3 == 1:
    height_value = input("Please Enter The Height Value: ")
    key3 = checkInputValue(height_value)
trapezoid_area_value = calculateTrapezoidArea(base1_value, base2_value, height_value)
print("Trapezoid Area: " + str(trapezoid_area_value))