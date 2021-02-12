import machine
import utime

potentiometer = machine.ADC(26)
conversion_factor = 3.3 / (65535)

while True:
  print(potentiometer.read_u16())
  utime.sleep(2)
  # print voltage
  voltage = potentiometer.read_u16() * conversion_factor
  print(voltage)
  utime.sleep(2)
