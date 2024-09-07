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

motors = robot.Motors()
right = motors.right_motor_pwm
left = motors.left_motor_pwm
right_dir = motors.right_motor_dir
left_dir = motors.left_motor_dir

# receiver PWM inputs
# interpret receiver inputs
# left_input = 
# right_input = 

# Display the interpreted receiver inputs
# Bottom of display = 64 pixels
# Top of plot = 40 pixels
# Max height of plot = 64-40 = 24 pixels
# left and right are a value between 0..1023
# left_dir and right_dir are 1 for forward and 0 for reverse
plot_top = 40
plot_height = 24
scale = plot_height/(1023*2)
zero_crossing = plot_top + (plot_height/2)

display.fill_rect(0, plot_top, 128, plot_height, 0)

display.fill_rect(36, 64-int(left_input*scale), 8, int(left_input*scale), 1)
display.fill_rect(84, 64-int(right_input*scale), 8, int(right_input*scale), 1)

display.show()