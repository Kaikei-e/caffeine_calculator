import sys
import matplotlib.pyplot as ppt
import datetime
from funcs import excp_handler
from funcs import caffe_cals
#sys.path.append('chronologiCal/funcs')

selected_mode = None

chronological_stmt = "Please enter multiple drinks in chronological order. The order can be in any order. The format should be 'YYYY/MM/DD H:M', such as '2020/12/01 21:34'."
check_drinks_stmt = "How many drinks do you want to calculate?"
mode_statement = "Mode 1 is calculated by the amount of caffeine per 100ml, Mode 2 is calculated by the total amount of the caffeine.\n Choose 1 or 2."
mode1_statement = "Enter first the amount of the drink and then the amount of caffeine per 100 ml, separated by a space"
mode2_statement = "Enter the total amount of caffeine in mg."


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
            dt_list.append(excp_handler.chrono_excp_handler())
        print("Formatted.")
        print("You entered these.\nIs this OK?\nEnter 'y' or 'n'.")
        for dt_l in dt_list:
            print(datetime_to_str(dt_l))
        flag_datetimes = excp_handler.yon_excp_handler(input())

    return dt_list


def chronological_cal(datetimes):
    for dt_l in datetimes:
        str_datetime = datetime.datetime.strftime(dt_l, '%Y/%m/%d %H:%M')
        print("Please select a calculation mode for this date and time.\n : {0}".format(str_datetime))
        selected_mode = excp_handler.mode_excp_handler()


        """ 
        Mode branching
        """

        if selected_mode == 1:

            """

            Mode 1
            """
            inputs = []
            inputs = excp_handler.value_excp_handler1()

            drink_amount = float(inputs[0])
            caffe_per_100ml = float(inputs[1])
            Residual_caffeine_level = drink_amount * caffe_per_100ml / 100

            time_global = 0

            try:
                R_c_l = int(Residual_caffeine_level)
            except ValueError:
                print('不正な値が入力されました: Invalid values entered.')

            returned_list = caffe_cals.calculator1(R_c_l, dt_l)
            

            


        elif selected_mode == 2:

            """
            Mode 2
            """
            
            value = excp_handler.value_excp_handler2()
            total_caffeine = float(value)
            Residual_caffeine_level = total_caffeine
            # Residual_caffeine_level = input()

            time_global = 0

            try:
                R_c_l = int(Residual_caffeine_level)
            except ValueError:
                print('不正な値が入力されました: Invalid values entered.')

            returned_list = caffe_cals.calculator2(R_c_l)
            
            




datetime_list = datetimes_loop(excp_handler.number_excp_handler())
datetime_list = sorted(datetime_list)

chronological_cal(datetime_list)


    
print(returned_list[0])
print(returned_list[1])

ppt.xlabel("Time(h)")
ppt.ylabel("Caffeine(mg)")
ppt.grid()
ppt.plot(returned_list[0], returned_list[1])

