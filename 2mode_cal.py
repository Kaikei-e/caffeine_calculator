import matplotlib.pyplot as ppt

mode_statement = "Please select a calculation method. Mode 1 is calculated by the amount of caffeine per 100ml, Mode 2 is calculated by the total amount of the caffeine.\n Choose 1 or 2."
mode1_statement = "Enter first the amount of the drink and then the amount of caffeine per 100 ml, separated by a space"
mode2_statement = "Enter the total amount of caffeine in mg."


selected_mode = None


def mode_excp_handler():
    flag_mode = True
    global selected_mode

    print(mode_statement)
    while flag_mode == True:
        try:
            selected_mode = int(input())
            if selected_mode < 1 or selected_mode > 2:
                print("Please enter 1 or 2")
            elif selected_mode == 1 or selected_mode == 2:
                flag_mode = False
        except:
            print(" An exception occurred.\nPlease enter 1 or 2.")

def value_excp_handler1():
    flag_value = True

    while flag_value == True:
        print(mode1_statement)
        s = input().rstrip().split()

        try:
            s[0] = float(s[0])
            s[1] = float(s[1])
            flag_value = False
        except:
            print("Please enter a number, not a string.")

    return s

def value_excp_handler2():
    flag_value = True

    while flag_value == True:
        print(mode2_statement)
        s = input()
        try:
            s = float(s)
            flag_value = False
        except:
            print("Please enter a number, not a string.")

    return s

def calculator1(caffeine):
        time_local = time_global
        time_list = []
        caffeine_list = []
        
        for i in range(caffeine):
            time_list.append([time_local])
            caffeine_list.append([caffeine])

            time_local += 5
            caffeine -= caffeine / 2


            if caffeine < 5:
                break
        return time_list, caffeine_list

def calculator2(caffeine):
        time_local = time_global
        time_list = []
        caffeine_list = []
        
        for i in range(caffeine):
            time_list.append([time_local])
            caffeine_list.append([caffeine])

            time_local += 5
            caffeine -= caffeine / 2


            if caffeine < 5:
                break
        return time_list, caffeine_list


mode_excp_handler()

""" 
Mode branching
"""

if selected_mode == 1:

    """

    Mode 1
    """
    #print(mode1_statement)

    ##############
    inputs = []
    inputs = value_excp_handler1()

    drink_amount = float(inputs[0])
    caffe_per_100ml = float(inputs[1])
    Residual_caffeine_level = drink_amount * caffe_per_100ml / 100

    time_global = 0

    try:
        R_c_l = int(Residual_caffeine_level)
    except ValueError:
        print('不正な値が入力されました: Invalid values entered.')

    returned_list = calculator1(R_c_l)
    

    


elif selected_mode == 2:

    """
    Mode 2
    """
    
    value = value_excp_handler2()
    ##############
    total_caffeine = float(value)
    Residual_caffeine_level = total_caffeine
    # Residual_caffeine_level = input()

    time_global = 0

    try:
        R_c_l = int(Residual_caffeine_level)
    except ValueError:
        print('不正な値が入力されました: Invalid values entered.')

    returned_list = calculator2(R_c_l)
    
    
print(returned_list[0])
print(returned_list[1])

ppt.xlabel("Time(h)")
ppt.ylabel("Caffeine(mg)")
ppt.grid()
ppt.plot(returned_list[0], returned_list[1])
