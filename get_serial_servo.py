#!/usr/bin/env python3
# encoding: utf-8

# This script is for AINEX Robot HeadNod. Since, nothing is directly from the UI
# This script is build by Mr Saad Jameel
# Contact: +92 333 3059002 (WhatsApp Only)
# E-mail: saadjamil1998@gmail.com


from ainex_sdk import hiwonder_servo_controller
servo_control = hiwonder_servo_controller.HiwonderServoController('/dev/ttyAMA0', 115200)


def get_status():
    servo_id = servo_control.get_servo_id()
   
    angle_range = servo_control.get_servo_range(servo_id)
    print('id:%s'%(str(servo_id).ljust(3)))
    print('angle_range:%s'%(str(angle_range).ljust(4)))
    

while True:
    try:
        get_status()
    
    except KeyboardInterrupt:
        break
