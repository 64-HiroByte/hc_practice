import datetime
import sys


def get_first_day_of_week(yr, mo):
    if yr and mo is not None:
        first_day = datetime.date(yr, mo, 1)
        first_day_of_week = datetime.date.weekday(first_day)
        return first_day_of_week


def get_last_day(yr, mo):
    if mo == 12:
        yr += 1
        mo = 1
    else:
        mo += 1
        
    last_day = datetime.date(year=yr, month=mo, day=1) - datetime.timedelta(days=1)
    return last_day.day


today = datetime.date.today()
current_year = today.year
current_month = today.month

# ここに引数を受け取った時の処理


# 引数の指定がなかった場合の年月
specified_year = current_year
specified_month = current_month
month_and_year =str(specified_month) + '月 ' + str(specified_year)

calendar_data = [[month_and_year.center(20)]]
first_day_index = get_first_day_of_week(yr=specified_year, mo=specified_month)
last_day_of_month = get_last_day(yr=specified_year, mo=specified_month)

DAY_NAME = ['月', '火', '水', '木', '金', '土', '日']

day_of_month = 1
calendar_data.append(DAY_NAME)
while day_of_month <= last_day_of_month:
    weekly_list = []
    for i in range(7):
        if day_of_month == 1 and i < first_day_index:
            str_value = ''
        else:
            str_value = str(day_of_month)
            day_of_month += 1
        str_value = f'{str_value:>2}'
        weekly_list.append(str_value)
        
        if day_of_month > last_day_of_month:
            break
    calendar_data.append(weekly_list)

for r in calendar_data:
    print(' '.join(r))
