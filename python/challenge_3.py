#Challenge 3 (use python 2) ini adalah membuat output seperti berikut:
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

high = input("Tinggi : ")
wide = input("Lebar : ")

while (high > 0):
	for i in range(wide):
		print(i+1),
	print("")
	high -= 1
	wide -= 1
