import os
from subprocess import run
from time import sleep
import sys

device_id = 'sdb1'


connected_user = run(['users'], capture_output=True).stdout.decode()
user = connected_user.strip()

print('[*] plug in the board')

while not device_id in os.listdir(f'/dev/'):
	sleep(0.5)


print('[*] board recognized')


print('[*] mounting the board to CIRCUITPY directory')
os.system(f'mount /dev/sdb1 /media/{user}/CIRCUITPY')

print('[*] wipping everything from the board')

try:

	os.remove(f'/media/{user}/CIRCUITPY/code.py')
except FileNotFoundError:
	print('[-] there was no payload on the board')
	os.system(f'umount -l  /dev/{device_id}')
	sys.exit(0)
os.system(f'umount -l /dev/{device_id}')

print('[*] done')



