"""
Created on Sat Aug  7 17:33:08 2021

@author: Yasin BİRCAN
"""

key = 1
pid_list = []
total_number = 0

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

while key == 1:
    number = input("Please enter the first number: ")
    key = checkInputValue(number)
number = int(number)

for i in range(int(number-1)):
    if number % (i+1) == 0:
        pid_list.append(i+1)
print("Proper integer divisiors of " + str(number) + ": " + str(pid_list))
for i in range(len(pid_list)):
    total_number = pid_list[i] + total_number
if total_number > number:
    print(str(number) + " is abundant number." )
else:
    print(str(number) + " is not abundant number.")