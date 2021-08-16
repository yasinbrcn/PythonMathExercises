"""
Created on Mon Aug 16 2021

@author: pc2
"""

key=1
key2=1
number_list=[]
even_number_list=[]
odd_number_list=[]
even_number = 0
odd_number = 0

def checkInputValue(r_value):
    try:
        r_value = int(r_value)
        if(r_value > 1):
            r_value_check = 0
        else:
            print("Please enter a number from grater than one.")
            r_value_check = 1
    except:
        try:
            r_value = float(r_value)
            print("Please enter integer value only. Not float value.")
            r_value_check = 1
        except:
            print("Please enter integer value only. Not string value.")
            r_value_check = 1
    return r_value_check

while key == 1:
    number = input("Please enter a number: ")
    key = checkInputValue(number)
number = int(number)

while number > 1:
    if number % 2 == 0:
        number = number/2
        even_number_list.append(int(number))
        number_list.append(int(number))
    elif number % 2 != 0:
        number = (3*number)+1
        odd_number_list.append(int(number))
        number_list.append(int(number))
print("Collatz Sequence: " + str(number_list) + " --> " + str(len(number_list)) + " steps")
print("List of Even Numbers: " + str(even_number_list) + " --> " + str(len(even_number_list)) + " pcs.")
print("List of Odd Numbers: " + str(odd_number_list) + " --> " + str(len(odd_number_list)) + " pcs.")