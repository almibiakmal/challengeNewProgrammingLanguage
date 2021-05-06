#Filter input pengguna
def filter_input(param,tipe,rule):
	#Deklarasi variabel status dan msg	
	status, msg = True, ""
	try:
		#Isi variabel data sesuai dengan tipe data
		if tipe == "integer": 
			data = int(param)
		else:
			data = param

		#Variabel rule merupakan sebuah array.
		#Lakukan pengecekan parameter sesuai dengan isi variabel rule.
		#Variabel rule dengan index ke-0 khusus menampung pesan utk error yg diakibatkan karena tidak sesuainya tipe data variabel param dengan tipe data yang ditentukan. Format variabel rule index ke-1 dan seterusnya adalah [key, value, errorMessage]
		for i in range(1, len(rule)):
			if (rule[i][0] == "min"):

				if data < rule[i][1]:
					status = False
					msg = rule[i][2]

			elif rule[i][0] == "empty":

				if data == "" or data == " ":
					status = False
					msg = rule[i][1]

	except ValueError:
		status = False
		msg = rule[0]
	return [status, data, msg]

#=====================Mulai================================
#Cetak pesan
print("Tentukan ukuran matrik terlebih dahulu")

#Mengatur nilai row matrik
while True:
	#Dapatkan input pengguna
	row = input("Baris: ")

	#Validasi input pengguna. Jika tidak valid maka tampilkan pesan error lalu mintak lagi inputan dari pengguna
	check = filter_input(row, "integer", [["Gagal, silahkan masukan angka...\n"],["min",1,"Gagal, baris harus lebih besar dari 0...\n"]])
	if check[0] == False:		
		print(check[2])
	else:
		row = check[1]
		break

#Mengatur nilai colom matrik
while True:
	colom = input("Kolom: ")
	check = filter_input(colom, "integer", [["Gagal, silahkan masukan angka...\n"],["min",1,"Gagal, kolom harus lebih besar dari 0...\n"]])
	if check[0] == False:		
		print(check[2])
	else:
		colom = check[1]
		break

print("")
matrik = []
for x in range(row):
	element = []
	for y in range(colom):
		while True:
			temp = input("Matrik [{},{}] : ".format((x+1),(y+1)))
			check = filter_input(temp, "", [[],["empty","Gagal, elemen matrik tidak boleh kosong!\n"]])
			if check[0] == False:		
				print(check[2])
			else:
				break
		element.append(check[1])
	matrik.append(element)

print("\nHasil :", matrik)
#=====================Selesai================================

