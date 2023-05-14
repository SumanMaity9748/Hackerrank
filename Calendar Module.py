import calendar

if __name__ == '__main__':
    m, d, y = map(int, input().strip().split(" "))
    print(calendar.day_name[calendar.weekday(y, m, d)].upper())
