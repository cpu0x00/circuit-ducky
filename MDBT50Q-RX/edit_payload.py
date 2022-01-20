import os
from subprocess import run
from time import sleep
import sys

connected_user = run(['users'], capture_output=True).stdout.decode()
user = connected_user.strip()

print('[*] plug in the board')

while not 'sdb1' in os.listdir(f'/dev/'):
	sleep(0.5)


print('[*] board recognized')


print('[*] mounting the board to CIRCUITPY directory')
os.system(f'mount /dev/sdb1 /media/{user}/CIRCUITPY')

print('[*] wipping everything from the board')

try:

	os.remove(f'/media/{user}/CIRCUITPY/code.py')
except FileNotFoundError:
	print('[-] there was no payload on the board')
	os.system('umount -l  /dev/sdb1')
	sys.exit(0)
os.system('umount -l /dev/sdb1')

print('[*] done')



