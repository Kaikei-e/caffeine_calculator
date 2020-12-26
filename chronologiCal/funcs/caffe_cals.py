time_global = 0

def calculator(caffeine, datetime):
        time_local = time_global
        time_list = []
        caffeine_list = []
        
        for i in range(caffeine):
            time_list.append(datetime)
            caffeine_list.append(caffeine)

            time_local += 5
            caffeine -= caffeine / 2


            if caffeine < 5:
                break
        return time_list, caffeine_list
