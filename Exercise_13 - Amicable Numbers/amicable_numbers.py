"""
Created on Tue Aug 17 2021

@author: Yasin BİRCAN
"""

key=1
pid_list = []
pid_list2 = []
number_list = []
amicable_numbers_list = []

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

def amicableNumberFinder(r_number): 
    total_number=0
    total_number_2=0
    for i in range(r_number-1):
        if r_number % (i+1) == 0:
            pid_list.append(i+1)
    for j in range(len(pid_list)):
        total_number = total_number + pid_list[j]
        
    for k in range(total_number-1):
        if total_number % (k+1) == 0:
            pid_list2.append(k+1)
    for l in range(len(pid_list2)):
        total_number_2 = total_number_2 + pid_list2[l]
        
    if total_number_2 == r_number and r_number != total_number:
        r_number_check = 1
    else:
        r_number_check = 0
    pid_list.clear()
    pid_list2.clear()
    return r_number_check

while key == 1:
    number = input("Please enter a number: ")
    key = checkInputValue(number)
number = int(number)
for m in range(1,number+1):
    number_list.append(m)
    if amicableNumberFinder(number_list[m-1]) == 1:
        amicable_numbers_list.append(number_list[m-1])
print("Amicable Number List: " + str(amicable_numbers_list))