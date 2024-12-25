#!/usr/bin/env python3
# encoding: utf-8
# This script is for AINEX Robot HeadNod. Since, nothing is directly from the UI
# This script is build by Mr Saad Jameel
# Contact: +92 333 3059002 (WhatsApp Only)
# E-mail: saadjamil1998@gmail.com

import time
from ainex_sdk import hiwonder_servo_controller

print('Head-Nod: ')
servo_control = hiwonder_servo_controller.HiwonderServoController('/dev/ttyAMA0', 115200)

def read_servo_position():
    positions = []
    for servo_id in range(1,25):
        pos = servo_control.get_servo_position(servo_id)
        
        positions.append(pos)
    return positions

duration = 500
try:
    data = []
    for cycle in range(1, 3):
        for headPos in [600, 500]:
            current_position = read_servo_position()
            # print(current_position)

            # Store data
            record = {"Time": duration}
            record.update({f"Servo{i+1}": positions[i] for i in range(24)})
            data.append(record)

            servo_control.set_servo_position(23, headPos, duration)
            time.sleep(1)
    print(data)

except KeyboardInterrupt:
    print("Program has Terminated")

# ServoMotion
