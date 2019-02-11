#Challenge 1 (use python 2) ini adalah membuat output seperti berikut:
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 

high = input("Tinggi : ")
wide = input("Lebar : ")

#Versi 1
print("Versi 1")

i=0
while (i < high):
	j = 0
	temp = ""
	while (j < wide):
		temp +=" *"
		j+=1

	print(temp)
	i+=1


#Versi 2
print("Versi 2")

while (high > 0):
	temp = ""
	l = wide
	while (l > 0):
		temp +=" *"
		l -= 1

	print(temp)
	high -= 1
