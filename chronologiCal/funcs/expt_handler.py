import datetime

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
