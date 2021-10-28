"""
Created on Thu Oct 28 23:30:32 2021

@author: Yasin BİRCAN
"""
key=1
fermat_number_list = []

def checkInputValue(r_value):
    try:
        r_value = int(r_value)
        if(r_value > 0):
            r_value_check = 0
        else:
            print("Please enter a number from grater than zero.")
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

for i in range(0,number):
    fermat_number_list.append(2**(2**i)+1)
    
print("Fermat Number List: " + str(fermat_number_list))
