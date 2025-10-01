import datetime

def is_restaurant_open():
    now = datetime.datetime.now()
    current_day = now.weekday()
    current_time = now.time()

    if current_day < 5:
        opening_time = datetime.time(9,0)
        closing_time = datetime.time(22,0)
    else:
        opening_time = datatime.time(10,0)
        closing_time = datetime.time(23,0)
    return opening_time <= current_time <=closing_time