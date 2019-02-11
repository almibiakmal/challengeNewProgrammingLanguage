import os

print("Welcome Bro")

while True:
	try:
		total_day = int(input("How many days in 1 week? "))

		#Get current directory
		dir_path = os.path.dirname(os.path.realpath(__file__))
		number = 1
		#Open file days.txt in directory temp
		file = open(dir_path + "/temp/days.txt", "w+")
		while(total_day > 0):
			while True:
				try:
					temp = str(input("Day {} : ".format(number)))

#					value = "Hari {} {} \n".format(number,temp)
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

