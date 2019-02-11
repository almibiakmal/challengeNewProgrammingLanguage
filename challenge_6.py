#Challenge 6 (use python 3)
#Next Level nya : cari tahu tipe data array di Python. Alur programnya : Anda minta user untuk memasukkan bilangan sebanyak yg user mau. Kalau proses memasukkan data nya mau diakhiri user harus memasukkan data karakter. Lalu Anda lakukan proses Sorting dan tampilkan ke layar data yg sebelum di sort dan setelah di Sort. Jangan googling metoda Sort, pakai metoda Anda sendiri utk melakukan Sorting. Yang pasti Sortingnya Ascending dan kalau value yg dibandingkan sama nilainya tidak usah di ubah posisinya. Misal 3, 1, 3, 4. Yang diubah hanya posisi 3 pertama tukar dengan angka 1, jadi 1,3,3,4.

print ("====================================\nWelcome to Sorting Program\n====================================\n")

angka = []
try:
	while True:
		temp = int(input("Enter a number : "))
		angka.append(temp)
except ValueError:
	print("Process input stoped.\n")

if len(angka) > 1:
	while True:
		answare = input("Do you want to start sorting (y/n) ? ")
		if answare == "y":
			print("Input : ", angka)
			print("Processing...")
			while True:
				move = 0
				for i in range(len(angka)-1):

					if angka[i] > angka[i+1]:
						temp = angka[i]
						angka[i] = angka[i+1]
						angka[i+1] = temp
						move += 1

				if move == 0:
					break

			print("Success...")
			print("Output : ", angka,"\n")
			break
		elif answare == "n":
			break
		else:
			print ("Unknow, please try again...\n")
else:
	if len(angka) == 1:
		print("Input : ", angka)
		print("Output : ", angka)
	else:
		print("Input is empty")

print ("Finish")
exit()
