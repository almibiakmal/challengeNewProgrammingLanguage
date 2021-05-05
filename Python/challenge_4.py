#Challenge 4 (use python 2) ini adalah membuat output seperti berikut:
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

lebar = input("Lebar : ")
limit = lebar
awal = False

while (True):
	for i in range(lebar):
		print(i+1),	

	print("")
	if(not awal):
		lebar -= 1
	if(lebar == 0):
		awal = True
	if(awal):
		if lebar == 0:
			lebar += 2
		else:
			lebar += 1
	if(lebar > limit):
		print("Selesai")
		break
