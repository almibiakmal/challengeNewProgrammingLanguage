import os
print("Welcome Bro")

while True:
	try:
		#Get total day from input user
		total_day = int(input("How many days in 1 week? "))

		#Get current directory
		dir_path = os.path.dirname(os.path.realpath(__file__))
		#Open file days.txt in directory temp
		file = open(dir_path + "/temp/days.txt", "w+")

		number = 1
		while(total_day > 0):
			while True:
				try:
					
#Get day's name from input user. If user not input a string than direct to bagian except (yang menampilkan tulisan "Please input a string..."
					temp = str(input("Day {} : ".format(number)))
					#Write day's name to file days.txt
					file.write("Hari {} {} \n".format(number,temp))
					number += 1
					total_day -= 1
					break

				except ValueError:
					print("Please input a string...")

		file.close()
		break
	except ValueError:
		print("Please input a number...")

print("Finished")

