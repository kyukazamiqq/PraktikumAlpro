#Nawwaf Abdurrahman
#122450018 

name = input("Name (First last) :")
file = input("Filename : ")

n = 6
list_grade = []

for i in range(1,n):
	print("Here are your randomly-selected grades (hope you pass): ")
	grade = input(f"grades {i} (1-100): ") 

	list_grade.append(grade)
	with open(f"{file}", "w") as f:
		f.write(str(name))
		f.write('\n')
		f.write(str(list_grade))


print(f"Data saved in '{file}''.")