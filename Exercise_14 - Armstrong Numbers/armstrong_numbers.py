"""
Created on Wed Aug 18 2021

@author: Yasin BİRCAN
"""
key2=1
number_list=[]
armstrong_number_list=[]
remainder_list=[]

def checkInputValue(r_value):
    try:
        r_value = int(r_value)
        r_value_check = 0
    except:
        try:
            r_value = float(r_value)
            print("Please enter integer value only. Not float value.")
            r_value_check = 1
        except:
            print("Please enter integer value only. Not string value.")
            r_value_check = 1
    return r_value_check

def armstrongNumberFinder(r_number):
    number2=r_number
    key=1
    counter=0
    toplam = 0
    while key == 1:
        remainder = number2 % 10
        remainder_list.append(remainder)
        number2 = int((number2 - remainder) / 10)
        counter = counter+1
        if number2 == 0:
            key = 0
    for i in range (len(remainder_list)):
        toplam = toplam + remainder_list[i]**len(remainder_list)
        if toplam == r_number:
            r_number_check = 1
        else:
            r_number_check = 0
    remainder_list.clear()
    return r_number_check

while key2 == 1:
    number = input("Bir sayı giriniz: ")
    key2 = checkInputValue(number)
number=int(number)
for j in range (1,number+1):
    number_list.append(j)
    if armstrongNumberFinder(number_list[j-1]) == 1:
        armstrong_number_list.append(number_list[j-1])
print("Armstrong Number List: " + str(armstrong_number_list))