"""
Created on Thu Oct 28 23:45:04 2021

@author: Yasin BİRCAN
"""

key=1
key2=1
number_list = []
leyland_number_list = []

def checkInputValue(r_value):
    try:
        r_value = int(r_value)
        if(r_value > 1):
            r_value_check = 0
        else:
            print("Please enter a number from grater than two.")
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

print("Leyland Numbers Formula: x^y+y^x")
while key == 1:
    x_number = input("Please enter the x number: ")
    y_number = input("Please enter the y number: ")
    if checkInputValue(x_number) == 0 and checkInputValue(y_number) == 0:
        key = 0
    else:
        key=1
x_number = int(x_number)
y_number = int(y_number)

for x in range(2,x_number+1):
    for y in range(2,y_number+1):
        number_list.append((x**y)+(y**x))

for k in range(len(number_list)):
  if number_list[k] not in leyland_number_list:
    leyland_number_list.append(number_list[k])
leyland_number_list.sort()
print("Leyland Numbers: " + str(leyland_number_list))