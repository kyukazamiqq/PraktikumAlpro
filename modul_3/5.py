n = 11
list_num = []

for i in range(1,n):
	num = int(input(f"Input number-{i} : "))
	list_num.append(num)

print(list_num)

cek_max = max(list_num)
print(f"The Largest Value is {cek_max}")
