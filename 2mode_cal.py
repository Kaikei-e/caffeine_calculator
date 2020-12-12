import matplotlib.pyplot as ppt

mode_statement = "Please select a calculation method. Mode 1 is calculated by the amount of caffeine per 100ml, Mode 2 is calculated by the total amount of the caffeine.\n Choose 1 or 2."

flag = True

while flag == True:
    print(mode_statement)
    try:
        selected_mode = int(input())
    except:
        print("Please enter 1 or 2.\n An exception occurred")
    else:
        flag = False

if selected_mode < 1 or selected_mode > 2:
    print("Please enter 1 or 2")
    selected_mode = input()


""" 
Mode branching
"""

if selected_mode == 1:

    """

    Mode 1
    """

    print("Enter first the amount of the drink and then the amount of caffeine per 100 ml, separated by a space")

    s = input().rstrip().split()
    drink_amount = float(s[0])
    caffe_per_100ml = float(s[1])
    Residual_caffeine_level = drink_amount * caffe_per_100ml / 100
    # Residual_caffeine_level = input()

    time_global = 0

    try:
        R_c_l = int(Residual_caffeine_level)
    except ValueError:
        print('不正な値が入力されました: Invalid values entered.')

    def calculator1(caffeine):
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


else:

    """
    Mode 2
    """
    print("Enter the total caffeine content of the drink.")
    s = input()
    total_caffeine = float(s)
    Residual_caffeine_level = total_caffeine
    # Residual_caffeine_level = input()

    time_global = 0

    try:
        R_c_l = int(Residual_caffeine_level)
    except ValueError:
        print('不正な値が入力されました: Invalid values entered.')

    def calculator2(caffeine):
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



if selected_mode == 1:
    returned_list = calculator1(R_c_l)
else:
    returned_list = calculator2(R_c_l)
    
print(returned_list[0])
print(returned_list[1])

ppt.plot(returned_list[0], returned_list[1])
