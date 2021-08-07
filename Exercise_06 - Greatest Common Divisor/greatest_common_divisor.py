"""
Created on Sat Aug  7 12:22:48 2021

@author: Yasin BİRCAN
"""
pid_list_1=[]
pid_list_2=[]
total_pid_list=[]
key_1 = 1
key_2 = 1

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
    
for i in range(int(number_1)):
    if number_1 % (i+1) == 0:
        pid_list_1.append(i+1)
print("Positive integer divisiors of " + str(number_1) + ": " + str(pid_list_1))
for i in range(number_2):
    if number_2 % (i+1) == 0:
        pid_list_2.append(i+1)
pid_list_1.extend(pid_list_2)
print("Positive integer divisiors of " + str(number_2) + ": " + str(pid_list_2))
for j in range(len(pid_list_1)):
    if pid_list_1.count(pid_list_1[j]) == 2 and pid_list_1[j] not in total_pid_list:
        total_pid_list.append(pid_list_1[j])
print("Greatest common divisior: " + str(total_pid_list[len(total_pid_list)-1]))
