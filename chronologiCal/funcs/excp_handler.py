import datetime

chronological_stmt = "Please enter multiple drinks in chronological order. The order can be in any order. The format should be 'YYYY/MM/DD H:M', such as '2020/12/01 21:34'."
check_drinks_stmt = "How many drinks do you want to calculate?"
mode_statement = "Mode 1 is calculated by the amount of caffeine per 100ml, Mode 2 is calculated by the total amount of the caffeine.\n Choose 1 or 2."
mode1_statement = "Enter first the amount of the drink and then the amount of caffeine per 100 ml, separated by a space"
mode2_statement = "Enter the total amount of caffeine in mg."

selected_mode = None

def number_excp_handler():
    flag_number = True
    print(check_drinks_stmt)
    while flag_number == True:
        try:
            number_of_drinks = int(input())
            if number_of_drinks < 1:
                print("Enter an integer greater than or equal to 1.")
            elif number_of_drinks > 0:
                flag_number = False
            return number_of_drinks
        except:
            print("An exception occurred.\nPlease enter integer.")

def chrono_excp_handler():
    flag_chrono = True
    #print(chronological_stmt)
    while flag_chrono == True:
        try:
            datetimes = input()
            dts = datetime.datetime.strptime(datetimes,'%Y/%m/%d %H:%M')
            flag_chrono = False
            return dts
        except:
            print("An exception occurred.\nPlease enter the correct form.")

def yon_excp_handler(y_o_n):
    global chronological_stmt
    flag_yon = True
    while flag_yon == True:
        if y_o_n == "y" or y_o_n == "Y":
            print("Ready to go!")
            flag_yon = False
            return False
        elif y_o_n == "n" or y_o_n == "N":
            print(chronological_stmt)
            return True


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
                return selected_mode
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
