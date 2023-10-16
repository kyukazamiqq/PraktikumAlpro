
n = 11
list_num = []

for i in range(1,n):
	num = input(f"Input number-{i} : ")
	list_num.append(num)

print(list_num)

choice = input("Do u want to check ur number ? ")

if choice == "no":
	print("Allright thats your choice, See ya!")
	exit()
elif choice == "yes":
	print("Allright, give me number to check : ")
	cek_num = input("> ")
	if cek_num in list_num:
		print(f"Yes, {cek_num} in the list enjoy!")
	else:
		print(f"Hmmmm, thas not in the freakin list, check again.")
else:
	print("please, just answer with yes or no.")