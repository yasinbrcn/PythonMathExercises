# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:49:40 2021

@author: Yasin BİRCAN
"""

pim_list_1=[]
pim_list_2=[]
total_pim_list=[]
key_1 = 1
key_2 = 1
new_number_1 = 0
new_number_2 = 0

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

while key_1 == 1:
    number_1 = input("Please enter the first number: ")
    key_1 = checkInputValue(number_1)
number_1 = int(number_1)

while key_2 == 1:
    number_2 = input("Please enter the second number: ")
    key_2 = checkInputValue(number_2)
number_2 = int(number_2)

for i in range(int(number_1*10)):
    new_number_1 = new_number_1 + number_1
    pim_list_1.append(new_number_1)
print("Positive integer multiple of " + str(number_1) + ": " + str(pim_list_1) + "...")

for i in range(int(number_2*10)):
    new_number_2 = new_number_2 + number_2
    pim_list_2.append(new_number_2)
print("Positive integer multiple of " + str(number_2) + ": " + str(pim_list_2) + "...")
pim_list_1.extend(pim_list_2)
for j in range(len(pim_list_1)):
    if pim_list_1.count(pim_list_1[j]) == 2 and pim_list_1[j] not in total_pim_list:
        total_pim_list.append(pim_list_1[j])
print("Least common multiple: " + str(total_pim_list[0]))