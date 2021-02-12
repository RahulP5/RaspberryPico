import machine
import utime

potentiometer = machine.ADC(26)
while True:
  print(potentiometer.read_u16())
  utime.sleep(2)
