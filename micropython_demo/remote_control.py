# This program will allow an operator to provide inputs via RC Transmitter
# to control the robot

from zumo_2040_robot import robot
import time

# Allow user to activate remote control mode and provide display to
# confirm that RC Transmitter is connected and configured as expected

display = robot.Display()
last_update = 0
# button_a = robot.ButtonA()
# button_b = robot.ButtonB()
# button_c = robot.ButtonC()

# motors = robot.Motors()
# right = motors.right_motor_pwm
# left = motors.left_motor_pwm
# right_dir = motors.right_motor_dir
# left_dir = motors.left_motor_dir

# while True:
#     t = time.ticks_ms()

# receiver PWM inputs
# interpret receiver inputs
left_input = 800
right_input = 200



# Display the interpreted receiver inputs
# Bottom of display = 64 pixels
# Top of plot = 40 pixels
# Max height of plot = 64-40 = 24 pixels
# left and right are a value between 0..1023
# left_dir and right_dir are 1 for forward and 0 for reverse
plot_top = 40
plot_height = 24
scale = plot_height / (1023 * 2)
zero_crossing = plot_top + (plot_height / 2)
left_plot_height = (left_input - 1023/2) * scale
right_plot_height = (right_input - 1023/2) * scale


display.fill_rect(0, plot_top, 128, plot_height, 0)

# h cannot be negative
if left_plot_height < 0:
    display.fill_rect(36, int(zero_crossing-left_plot_height), 8, int(abs(left_plot_height)), 1)
    display.text(str(int(left_plot_height)), 0, int(zero_crossing), 1)
else:
    display.fill_rect(36, int(zero_crossing), 8, int(left_plot_height), 1)
    display.text(str(int(left_plot_height)), 0, int(zero_crossing), 1)

if right_plot_height < 0:
    display.fill_rect(84, int(zero_crossing-right_plot_height), 8, int(abs(right_plot_height)), 1)
    display.text(str(int(right_plot_height)), 92, int(zero_crossing), 1)

else:
    display.fill_rect(84, int(zero_crossing), 8, int(right_plot_height), 1)
    display.text(str(int(right_plot_height)), 92, int(zero_crossing), 1)

display.show()