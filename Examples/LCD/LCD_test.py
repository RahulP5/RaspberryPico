import utime

from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

print("Running test_main")
i2c = I2C(1, sda=machine.Pin(26), scl=machine.Pin(27), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
lcd.putstr("It Works!")
utime.sleep(2)
lcd.clear()

while True:
        lcd.clear()
        time = utime.localtime()
        lcd.putstr("{year}/{month}/{day} {HH}:{MM}:{SS}".format(
            year=str(time[0]), month=str(time[1]), day=str(time[2]),
            HH=str(time[3]), MM=str(time[4]), SS=str(time[5])))
        utime.sleep(2)
