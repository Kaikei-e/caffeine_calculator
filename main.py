import matplotlib.pyplot as ppt

statement = "Enter first the amount of the drink and then the amount of caffeine per 100 ml, separated by a space"

def value_excp_handler():
    flag_value = True

    while flag_value == True:
        print(statement)
        s = input().rstrip().split()

        try:
            s[0] = float(s[0])
            s[1] = float(s[1])
            flag_value = False
        except:
            print("Please enter a number, not a string.")

    return s

inputs = []
inputs = value_excp_handler()

drink_amount = float(inputs[0])
caffe_per_100ml = float(inputs[1])
Residual_caffeine_level = drink_amount * caffe_per_100ml / 100
# Residual_caffeine_level = input()

time_global = 0

try:
    R_c_l = int(Residual_caffeine_level)
except ValueError:
    print('不正な値が入力されました: Invalid values entered.')

def calculator(caffeine):
    time_local = time_global
    time_list = []
    caffeine_list = []
    
    for i in range(caffeine):
        time_list.append([time_local])
        caffeine_list.append([caffeine])

        time_local += 6
        caffeine -= caffeine / 2


        if caffeine < 5:
            break
    return time_list, caffeine_list




returned_list = calculator(R_c_l)

    
print(returned_list[0])
print(returned_list[1])

ppt.plot(returned_list[0], returned_list[1])

