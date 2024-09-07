# This program will allow an operator to provide inputs via RC Transmitter
# to control the robot

from zumo_2040_robot import robot

# Allow user to activate remote control mode and provide display to
# confirm that RC Transmitter is connected and configured as expected

display = robot.Display()
last_update = 0
# button_a = robot.ButtonA()
# button_b = robot.ButtonB()
# button_c = robot.ButtonC()

# interpret receiver inputs


# Display the interpreted receiver inputs
# Top of display = 64 pixels
# Top of rectangle = 40 pixels
# Max height of rectangle = 64-40 = 24 pixels
# left or right are numbers with a value between -1023..1023
scale = 24/(2*1023)

display.fill_rect(0, 40, 128, 24, 0)

display.fill_rect(36, 64-int(left[0]*scale), 8, int(left[0]*scale), 1)
display.fill_rect(84, 64-int(right[0]*scale), 8, int(right[0]*scale), 1)

display.show()