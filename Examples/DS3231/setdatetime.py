import urtc
from machine import I2C, Pin
from utime import sleep

i2c = I2C(1,scl=Pin(27), sda=Pin(26))
rtc = urtc.DS3231(i2c)

datetime = rtc.datetime()

sw1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
sw2 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

day = datetime.day
month = datetime.month
year = datetime.year
hour = datetime.hour
minute = datetime.minute

print("{0}/{1}/{2}    {3}:{4}".format(day, month, year, hour, minute))

while True:
    if sw1.value() == 0:
        modify = 0
        print(day)
        print("in mode")
        while True:
            #print(sw2.value())
            if sw2.value() == 0 and modify == 0:
                print("day modify")
                while True:
                    print(day)
                    sleep(0.2)
                    if sw1.value() == 0:
                        day += 1
                        if day >= 32:
                            day = 1
                    if sw2.value() == 0:
                        modify = 1
                        print(month)
                        sleep(0.5)
                        break
            if sw2.value() == 0 and modify == 1:
                print("month modify")
                while True:
                    print(month)
                    sleep(0.2)
                    if sw1.value() == 0:
                        month += 1
                        if month >= 13:
                            month = 1
                    if sw2.value() == 0:
                        modify = 2
                        print(year)
                        sleep(0.5)
                        break
            if sw2.value() == 0 and modify == 2:
                while True:
                    print(year)
                    sleep(0.2)
                    if sw1.value() == 0:
                        year += 1
                        if year >= 2041:
                            year = 2021
                    if sw2.value() == 0:
                        modify = 3
                        print(hour)
                        sleep(0.5)
                        break
            if sw2.value() ==0 and modify == 3:
                while True:
                    print(hour)
                    sleep(0.2)
                    if sw1.value() == 0:
                        hour += 1
                        if hour >= 25:
                            hour = 00
                    if sw2.value() == 0:
                        modify = 4
                        print(minute)
                        sleep(0.5)
                        break
            if sw2.value() == 0 and modify == 4:
                while True:
                    print(minute)
                    sleep(0.2)
                    if sw1.value() == 0:
                        minute += 1
                        if minute >= 60:
                            minute = 00
                    if sw2.value() == 0:
                        modify = 5
                        break
            if modify == 5:
                print(" hour", hour )
                datetime = urtc.datetime_tuple(year=year, month=month, day=day, hour = hour, minute = minute, second = 10)
                rtc.datetime(datetime)
                datetime = rtc.datetime()
                print("complited")
                break
    
    else:
        datetime = rtc.datetime()
        print("{0}/{1}/{2}    {3}:{4}".format(datetime.day, datetime.month, datetime.year, datetime.hour, datetime.minute))
        sleep(1)
        
                
        
    
