# changing ducky payloads to circuitpython
# Author: Karim (mr.nobody) 


import sys

payload = sys.argv[1]

duckypayload = open(payload, 'r', encoding='latin1').readlines()

file = []

chars = ['a',
		'b',
		'c',
		'd',
		'e',
		'f',
		'g',
		'h',
		'i',
		'j',
		'k',
		'l',
		'm',
		'o',
		'p',
		'q',
		'r',
		's',
		't',
		'u',
		'v',
		'w',
		'x',
		'y',
		'z',
		'F1',
		'F2',
		'F3',
		'F4',
		'F5',
		'F6',
		'F7',
		'F8',
		'F9',
		'F10',
		'F11',
		'F12'

]


ducky_commands = {
	
	'WINDOWS': 'Keycode.WINDOWS', 
	'COMMAND': 'Keycode.WINDOWS',
	'GUI': 'Keycode.GUI',
	'APP': 'Keycode.APPLICATION', 
	'MENU': 'Keycode.APPLICATION', 
	'SHIFT': 'Keycode.SHIFT',
	'ALT': 'Keycode.ALT', 
	'CONTROL': 'Keycode.CONTROL', 
	'CTRL': 'Keycode.CONTROL',
	'DOWNARROW': 'Keycode.DOWN_ARROW', 
	'DOWN': 'Keycode.DOWN_ARROW', 
	'LEFTARROW': 'Keycode.LEFT_ARROW',
	'LEFT': 'Keycode.LEFT_ARROW',
	'RIGHTARROW': 'Keycode.RIGHT_ARROW', 
	'RIGHT': 'Keycode.RIGHT_ARROW',
	'UPARROW': 'Keycode.UP_ARROW',
	'UP': 'Keycode.UP_ARROW',
	'BREAK': 'Keycode.PAUSE',
	'PAUSE': 'Keycode.PAUSE',
	'CAPSLOCK': 'Keycode.CAPS_LOCK',
	'DELETE': 'Keycode.DELETE',
	'END': 'Keycode.END',
	'ESC': 'Keycode.ESCAPE', 
	'ESCAPE': 'Keycode.ESCAPE',
	'HOME': 'Keycode.HOME',
	'INSERT': 'Keycode.INSERT',
	'NUMLOCK': 'Keycode.KEYPAD_NUMLOCK',
	'PAGEUP': 'Keycode.PAGE_UP',
	'PAGEDOWN': 'Keycode.PAGE_DOWN',
	'PRINTSCREEN': 'Keycode.PRINT_SCREEN',
	'ENTER': 'Keycode.ENTER',
	'SCROLLLOCK': 'Keycode.SCROLL_LOCK',
	'SPACE': 'Keycode.SPACE', 
	'TAB': 'Keycode.TAB',
	
}








for line in duckypayload:
	if 'STRING' in line:
		l = line.replace('STRING ', '')
		new_line = l.replace('\n', '')
		if '"' in new_line:

			cp_line = f"layout.write(r'{new_line}')"
			file.append(cp_line)
		if "'" in new_line:
			cp_line = f'layout.write(r"{new_line}")'
			file.append(cp_line)

		if not "'" in new_line and '"' not in new_line:
			cp_line = f"layout.write(r'{new_line}')"
			file.append(cp_line)
		

	if 'DELAY' in line:
		l = line.replace('DELAY ', '')
		new_line = l.replace('\n', '')
		cp_line = f'sleep({int(new_line)/1000})'
		file.append(cp_line)


	if 'REM' in line:
		l = line.replace('REM','#')
		cp_line = l.replace('\n','')
		file.append(cp_line)

	if line[0:6] == 'REPEAT':
		l = line.replace('REPEAT','')
		new_line = l.replace('\n','')
		if new_line == '':
			previous_line = len(file) - 1
			cp_line = file[previous_line]
			file.append(cp_line)
		if new_line != '':
			previous_line = len(file) - 1
			cp_line = file[previous_line]
			for _ in range(int(new_line)):

				file.append(cp_line)		 
	


	for key, value in ducky_commands.items():
		for char in chars:
			if key in line and char in line:

				sl = line.split()
				
				

				k1 = ducky_commands.get(sl[0])
				k2 = f'Keycode.{sl[1].upper()}'
				cp_line = f'kbd.send({k1}, {k2})' 
				file.append(cp_line)
					

		try:
			if key in line:
				
				try:

					line = line.split()
					

					

				except AttributeError:
					if line[2] != key:
						k1 = ducky_commands.get(line[0])
						k2 = ducky_commands.get(line[1])
						k3 = f'Keycode.{line[2].upper()}'
						cp_line = f'kbd.send({k1}, {k2}, {k3})'
						file.append(cp_line)						
					

		except IndexError as e:
			if not line[1]:

				cp_line = f'kbd.send({value})' 
				
				file.append(cp_line)

			if line[1]:

				k1 = ducky_commands.get(line[0])
				k2 = ducky_commands.get(line[1])
				cp_line = f'kbd.send({k1}, {k2})'
				file.append(cp_line)	
		
		if key in line:
			try:

				line = line.split()
			except AttributeError:

				try:

					if line[0] and not line[1] and not line[3]:
						pass
				except IndexError:

					cp_line = f'kbd.send({value})' 
				
					file.append(cp_line)

		
			
			



libs = '''import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode
from time import sleep


kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# ducky payload starts here

'''

name = 'code.py'

write_libs = open(name, 'w').write(libs)

write_payload = open(name, 'a').write('\n'.join(file))

write_libs = open(name, 'a').write('\n')

if write_payload:
	print(f'[*] circuitpython payload generated in {name} file')
