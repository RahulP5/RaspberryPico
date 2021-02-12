import machine
import utime

#Set up the analogue-to-digital converter again, but this time rather than using the number of a pin, use the channel number connected to the temperature sensor:
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
while True:
  reading = sensor_temp.read_u16() * conversion_factor
  temperature = 27 - (reading - 0.706)/0.001721
  print(temperature)
  utime.sleep(2)
