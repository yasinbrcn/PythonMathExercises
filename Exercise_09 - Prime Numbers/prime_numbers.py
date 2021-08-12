"""
Created on Wed Aug 11 2021

@author: Yasin BİRCAN
"""
number_list=[]
number_list_2=[]
prime_number_list=[]
key = 1

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

for i in range(2,number+1):
    number_list.append(i)
    
for j in range(len(number_list)):
    for k in range(2,len(number_list)+1):
        if number_list[j] % k == 0:
            number_list_2.append(number_list[j])
for l in range(len(number_list_2)):
    if number_list_2.count(number_list_2[l])==1:
        prime_number_list.append(number_list_2[l])
print("Prime Numbers: " + str(prime_number_list))
