import utime
import urtc
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

rtc_add = 0x68


i2c = I2C(1, sda=machine.Pin(26), scl=machine.Pin(27), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
rtc = urtc.DS3231(i2c, rtc_add)
lcd.putstr("Welcome")
utime.sleep(2)
lcd.clear()

while True:
    lcd.clear()
    datetime = rtc.datetime()
    day = datetime.day
    month = datetime.month
    year = datetime.year
    hour = datetime.hour
    minute = datetime.minute
    time = utime.localtime()
    #print("{0}/{1}/{2}    {3}:{4}".format(day, month, year, hour, minute))
    lcd.putstr("{day}/{month}/{year} \n{HH}:{MM}".format(day=day, month=month, year=year, HH=hour, MM=minute))
    utime.sleep(2)
    
