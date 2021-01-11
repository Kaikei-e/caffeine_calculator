import datetime

time_global = 0

def compare_calculator(caffeine, datetime1, datetime2):
        time_local = time_global
        time_list = []
        caffeine_list = []
        caffeine = int(caffeine)
        caffe_decay = 0.97716

        for i in range(500):
            if datetime1 >= datetime2:
                break
            
            time_list.append(datetime1)
            caffeine_list.append(caffeine)

            datetime1 += datetime.timedelta(minutes=10)
            caffeine = caffeine * caffe_decay

            if caffeine < 5:
                break

        return time_list, caffeine_list, caffeine


def simple_calculator(caffeine, datetime1):
    time_local = time_global
    time_list = []
    caffeine_list = []
    caffeine = int(caffeine)
    caffe_decay = 0.97716

    
    for i in range(500):
        time_list.append(datetime1)
        caffeine_list.append(caffeine)

        datetime1 += datetime.timedelta(minutes=10)
        caffeine = caffeine * caffe_decay

        if caffeine < 5:
            break

    return time_list, caffeine_list