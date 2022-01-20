# python script to automate the creation of a usb rubber ducky with a resperry pi pico

import os
from subprocess import run
from time import sleep
import sys

try:

	device_id = 'sdb1'
	connected_user = run(['users'], capture_output=True).stdout.decode()
	user = connected_user.strip()
	flash_script = '/opt/pico-to-ducky/adafruit7/flash_nuke.uf2'
	circuitpyuf2 = '/opt/pico-to-ducky/adafruit7/adafruit-circuitpython-raspberry_pi_pico-en_US-7.0.0.uf2'
	hid_lib = '/opt/pico-to-ducky/adafruit7/adafruit_hid'
	dip = sys.argv[2]
	payload = sys.argv[1]


	def mount_rpi():
		print('[*] mounting the pico to RPI-RP2 directory')
		os.system(f'mount /dev/{device_id} /media/{user}/RPI-RP2')


	def unmount_device():
		print('[*] unmounting the pico')
		os.system(f'umount /dev/{device_id}')	


	def mount_circuitpy():
		print('[*] mounting the pico to CIRCUITPY directory')
		os.system(f'mount /dev/{device_id} /media/{user}/CIRCUITPY')



	def create_ducky():

		print('[*] plug in the pico')
		while not device_id in os.listdir('/dev/'):
			sleep(0.5)

		mount_rpi()
		print('[*] using the flash_nuke.uf2 script to format the pico')

		os.system(f'cp {flash_script} /media/{user}/RPI-RP2/')
		while device_id in os.listdir(f'/dev/'): 
			sleep(0.5)
		
		unmount_device()

		print('[*] waiting for the pico to come up')
		while not device_id in os.listdir(f'/dev/'):
			sleep(0.5)

		print('[*] the pico is up !')
		mount_rpi()
		print('[*] copying the adafruit circuitpython file to the pico')

		os.system(f'cp {circuitpyuf2} /media/{user}/RPI-RP2/')
		while device_id in os.listdir(f'/dev/'): 
			sleep(0.5)

		unmount_device()
		print('[*] waiting for the pico to come up as CIRCUITPY device')
		while not device_id in os.listdir(f'/dev/'):
			sleep(0.5)

		mount_circuitpy()

		print('[*] removing unneccessary files from the pico')
		sleep(2)
		os.system(f'rm /media/{user}/CIRCUITPY/code.py')
		os.system(f'rm /media/{user}/CIRCUITPY/boot_out.txt')

		print("[*] putting the (adafruit_hid) into the pico's lib folder")

		os.system(f'cp -r {hid_lib} /media/{user}/CIRCUITPY/lib/')

		print('[*] copying the duckyinpython script to the pico as code.py')

		os.system(f'cp {dip} /media/{user}/CIRCUITPY/code.py')

		print('[*] copying the payload to the pico')

		os.system(f'cp {payload} /media/{user}/CIRCUITPY/')

		print('[*] the pico is ready')
		# print("\n[i] don't forget to unmount sdb1 after taking out the pico (umount /dev/sdb1)")
		os.system(f'umount /dev/{device_id}')

	

	create_ducky()

except IndexError:
	print('[-] python3 pico_to_ducky.py <payload.dd> </path/to/duckyinpython.py>')