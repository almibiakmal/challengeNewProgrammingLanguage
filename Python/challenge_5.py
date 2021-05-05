#Challenge 5 (use python 2) ini adalah membuat output seperti berikut:
# 1 2 3 4 5 6
# 2 4 6 8 10
# 7 8 9 10
# 12 14 16
# 11 12
# 18

lebar = input("Lebar : ")

nomor = 1
pointerGenap = 0
row = 1

while (True):
	i = lebar
	while (True):

		if row > 1:

			if row % 2 == 0:
				if pointerGenap == 0:

					if nomor % 2 == 0:
						print (nomor),
						i -= 1	

					nomor += 1
					if i == 0:
						pointerGenap = nomor
						break
				else:
					if pointerGenap % 2 == 0:
						print (pointerGenap),
						i -= 1
					pointerGenap += 1

					if i == 0:
						break
			elif row % 2 != 0:
				print (pointerAsli),
				pointerAsli += 1
				i -= 1

				if i == 0:
					break
		else:
			print (nomor),
			nomor += 1

			if nomor > i:
				pointerAsli = nomor
				nomor = 1
				break
	print("")
	lebar -= 1
	row += 1

	if lebar == 0:
		break

