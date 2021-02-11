import machine
import utime

file = open("test.txt")
x = file.read()
file.close()

utime.sleep(2)
file = open("test.txt", "W")
file.write("1200")
file.close()
print(x)
print(type(x))
