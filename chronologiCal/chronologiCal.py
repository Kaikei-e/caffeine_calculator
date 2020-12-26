import sys
import matplotlib.pyplot as ppt
import datetime
import chronologiCal.funcs
#sys.path.append('chronologiCal/funcs')

chronological_stmt = "Please enter multiple drinks in chronological order. The order can be in any order. The format should be 'YYYY/MM/DD H:M', such as '2020/12/01 21:34'."
check_drinks_stmt = "How many drinks do you want to calculate?"
mode_statement = "Please select a calculation method. Mode 1 is calculated by the amount of caffeine per 100ml, Mode 2 is calculated by the total amount of the caffeine.\n Choose 1 or 2."
mode1_statement = "Enter first the amount of the drink and then the amount of caffeine per 100 ml, separated by a space"
mode2_statement = "Enter the total amount of caffeine in mg."

#drinks_list = []
selected_mode = None

def datetimes_loop(N_o_D):
    global chronological_stmt
    dt_list = []
    dt_l = None
    def datetime_to_str(datetimes):
        str_datetime = datetime.datetime.strftime(datetimes, '%Y/%m/%d %H:%M')
        return str_datetime
    flag_datetimes = True
    print(chronological_stmt)

    while flag_datetimes == True:
        for i in range(N_o_D):
            dt_list.append(chrono_excp_handler())

        for dt_l in dt_list:
            print(datetime_to_str(dt_l))
        print("\nYou entered these.\nIs this OK?\nEnter 'y' or 'n'.")
        flag_datetimes = yon_excp_handler(input())

    return dt_list

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
            print("An exception occurred.\nPlease enter 1 or 2.")

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


def chronological_cal(datetimes):
    for dt_l in datetimes:
        str_datetime = datetime.datetime.strftime(datetimes, '%Y/%m/%d %H:%M')
        print("Please select a calculation mode for this date and time.\n : {0}".format(str_datetime))
        mode_excp_handler()


        """ 
        Mode branching
        """

        if selected_mode == 1:

            """

            Mode 1
            """

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
            
            




datetime_list = datetimes_loop(number_excp_handler())
datetime_list = sorted(datetime_list)

chronological_cal(datetime_list)


"""
Drinks
"""
