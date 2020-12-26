from funcs import excp_handler
from funcs import caffe_cals

def mode_selecter(mode_num):
    """ 
    Mode branching
    """
    if mode_num == 1:
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
        return R_c_l

        
        
    elif mode_num == 2:
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
        return R_c_l
        
        
