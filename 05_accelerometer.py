from microbit import *

while True:
   reading = accelerometer.get_x()
   if reading > 50:
       display.show("R")
   elif reading < -50:
       display.show("L")
   else:
       display.show("-")
