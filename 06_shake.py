from microbit import display, Image, accelerometer, sleep
display.show(Image.HAPPY)

# if you shake the device, you make microbit sad
while True:
   if accelerometer.was_gesture('shake'):
       display.show(Image.SAD)
       sleep(2000)
       display.show(Image.HAPPY)
