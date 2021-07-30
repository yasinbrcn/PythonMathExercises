"""
Created on Fri Jul 30 07:39:52 2021

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

def calculateParallelogramArea(r_base_value, r_height):
    parallelogram_area = float(r_base_value)*float(r_height)
    return parallelogram_area

def calculateParallelogramPerimeter(r_side_value,r_base_value):
    parallelogram_perimeter = 2*float(r_side_value)+2*float(r_base_value)
    return parallelogram_perimeter

while key == 1:
    base_value = input("Please Enter The Base Length of the Parallelogram: ")
    key = checkInputValue(base_value)
while key2 == 1:
    side_value = input("Please Enter The Side Length of the Parallegrom: ")
    key2 = checkInputValue(side_value)
while key3 == 1:
    height_value = input("Please Enter The Height Value of the Parallegrom: ")
    key3 = checkInputValue(height_value)
parallelogram_area_value = calculateParallelogramArea(base_value,height_value)
parallelogram_perimeter_value = calculateParallelogramPerimeter(side_value,base_value)
print("Area of Parallelogram: " + str(parallelogram_area_value))
print("Perimeter of Parallelogram: " + str(parallelogram_perimeter_value))
