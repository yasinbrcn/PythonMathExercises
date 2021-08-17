"""
Created on Sat Aug  7 2021

@author: Yasin BİRCAN
"""

key = 1
pid_list = []
total_number = 0
number_list = []
abundant_numbers_list = []

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
            print("Please enter integer value only. Not string value.")
            r_value_check = 1
        except:
            print("Please enter integer value only. Not string value.")
            r_value_check = 1
    return r_value_check

def abundant_number_finder(r_number):
    total_number = 0
    for i in range(int(r_number-1)):
        if r_number % (i+1) == 0:
            pid_list.append(i+1)
    for j in range(len(pid_list)):
        total_number = pid_list[j] + total_number
    if total_number > r_number:
        r_number_check = 1
    else:
        r_number_check = 0
    pid_list.clear()
    return r_number_check

while key == 1:
    number = input("Please enter a number: ")
    key = checkInputValue(number)
number = int(number)
for k in range(1,number+1):
    number_list.append(k)
    if abundant_number_finder(number_list[k-1]) == 1:
        abundant_numbers_list.append(number_list[k-1])
print("Abundant Number List: " + str(abundant_numbers_list))