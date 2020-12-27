import sys
import matplotlib.pyplot as ppt
import datetime
from funcs import excp_handler
from funcs import caffe_cals
from funcs import mode_selecter
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


def chronological_cal(datetime_list):
    index = 0
    returned_time_list = []
    returned_recaffe_list = []
    rest_of_caffe = 0
    returned_list = []
    caffe_amount = 0
    caffe_caled = 0
    for dt_l in datetime_list:

        index += 1
        str_datetime = datetime.datetime.strftime(dt_l, '%Y/%m/%d %H:%M')
        print("Please select a calculation mode for this date and time.\n : {0}".format(str_datetime))
        selected_mode = excp_handler.mode_excp_handler()
        caffe_amount = mode_selecter.mode_selecter(selected_mode)
        if index < len(datetime_list):
            re_list = caffe_cals.compare_calculator(caffe_amount, dt_l, datetime_list[index])
            returned_list.insert(0, re_list[0])
            returned_list.insert(1, re_list[1])
            caffe_caled += returned_list[2]
            continue

        if index >= len(datetime_list) - 1:
            caffe_caled += caffe_amount
            re_list = caffe_cals.simple_calculator(caffe_caled, dt_l)
            returned_list.insert(0, re_list[0])
            returned_list.insert(1, re_list[1])

            continue


datetime_list = datetimes_loop(excp_handler.number_excp_handler())
datetime_list = sorted(datetime_list)

chronological_cal(datetime_list)


    
print(returned_list[0])
print(returned_list[1])

ppt.xlabel("Time(h)")
ppt.ylabel("Caffeine(mg)")
ppt.grid()
ppt.plot(returned_list[0], returned_list[1])

