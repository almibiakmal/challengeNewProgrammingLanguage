#Challenge 7 (use python 2)
#Next : Bikin sesuatu yg Fun. Cari tahu perintah utk tulis sesuatu ke satu lokasi tertentu di layar(boleh memanfaatkan fitur bawaan bahasa yg Anda pakai atau pun pakai trik anda sendiri), perintah bersihkan layar, dan perintah Delay (perintah utk menunda beberaps detik eksekusi perintah berikutnya). Yang harus Anda buat pertama adalah. Menampilkan karakter yg seakan akan jalan ke kanan sampai kolom terahir (biasanya sih kolom 80) setelah kolom terahir tercapai, maka karakter tersebut harus bergerak mundur sampai kolom 1, balik lagi dan seterusnya sampai ditekan hruf X (exit). Have Fun!

import sys; import os; import time;

#function untuk menampilkan karakter
def print_specific_location(x, y, karakter):
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, karakter))
	sys.stdout.flush()
#function untuk delay dan membersihkan layar
def delay_run(timeBreak):
	time.sleep(timeBreak)
	os.system('clear')
print("=============================================")
print("WELCOME TO THE BBF PROGRAM")
print("Created with Python")
print("=============================================")
karakter	= input("Masukan karakter : ")
sizeScreen	= os.popen('stty size', 'r').read().split()
tinggi		= 2
jarak		= 0
batas		= int(sizeScreen[1])
#batas		= 44
maju		= True
timeBreak	= 0.1

while True:
	if maju:
		if jarak == batas:
			maju = False
		else:
			jarak += 1
			print_specific_location(tinggi, jarak, karakter)
			delay_run(timeBreak)
	else:
		if jarak == 1:
			maju = True
		else:
			jarak -= 1
			print_specific_location(tinggi, jarak, karakter)
			delay_run(timeBreak)
