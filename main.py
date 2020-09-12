import matplotlib.pyplot as ppt



drink_amount = 355
caffe_per_100ml = 40
Residual_caffeine_level = drink_amount * caffe_per_100ml / 100
# Residual_caffeine_level = input()

time_global = 0

try:
    R_c_l = int(Residual_caffeine_level)
except ValueError:
    print('不正な値が入力されました')

def calculator(caffeine):
    time_local = time_global
    time_list = []
    caffeine_list = []
    
    for i in range(caffeine):
        time_local += 6
        caffeine -= caffeine / 2

        time_list.append([time_local])
        caffeine_list.append([caffeine])


        if caffeine < 5:
            break
    return time_list, caffeine_list


returned_list = calculator(R_c_l)

    
print(returned_list[0])
print(returned_list[1])

ppt.plot(returned_list[0], returned_list[1], '.')

