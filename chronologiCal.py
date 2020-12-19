import matplotlib.pyplot as ppt

chronological_stmt = "Please enter multiple drinks in chronological order. The order can be in any order. The format should be 'YYYY/MM/DD H:M', such as '2020/12/01 21:34'."
check_drinks_stmt = "How many drinks do you want to calculate?"
mode_statement = "Please select a calculation method. Mode 1 is calculated by the amount of caffeine per 100ml, Mode 2 is calculated by the total amount of the caffeine.\n Choose 1 or 2."
mode1_statement = "Enter first the amount of the drink and then the amount of caffeine per 100 ml, separated by a space"
mode2_statement = "Enter the total amount of caffeine in mg."

drinks_list = []
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
        except:
            print("An exception occurred.\nPlease enter integer.")

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


number_excp_handler()

"""

"""