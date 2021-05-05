#Failed, just for testing

angka = [1,8,4,3,9]
#max,min,head,tail

jumlahData = len(angka)
minimal = []
maksimal = []
mulai = 0

pointer = 0
while (pointer < jumlahData):
	if pointer == 0
		minimal.insert(0, mulai)		
		minimal.insert(1, angka[mulai])

		maksimal.insert(0, mulai)		
		maksimal.insert(1, angka[mulai])

		head = mulai
		tail = (jumlahData - 1)
	else:
		if angka[mulai] < minimal[1]:
			minimal.insert(0, mulai)
			minimal.insert(1, angka[mulai])

		if angka[mulai] > maksimal[1]:
			maksimal.insert(0, mulai)	
			maksimal.insert(1, angka[mulai])

	pointer += 1
	mulai += 1

if minimal[0] != head:
	temp = angka[head]
	angka[head] = angka[minimal[0]]
	angka[minimal[0]] = temp

if maksimal[0] != tail:
	temp = angka[tail]
	angka[tail] = angka[maksimal[0]]
	angka[maksimal[0]] = temp

head += 1
tail -= 1
mulai = head
jumlahData = 2
