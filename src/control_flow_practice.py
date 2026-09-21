# Week 2 - Python Control Flow Practice

age = 20

if age >= 18:
	print("valid age")
else:
	print("Invalid age")

print("--------------------")

names = ["John", "", "Sarah", "David"]

for name in names:
	if name == "":
		print("Empty name found")
	else:
		print("Valid name:", name)

print("--------------------")

def is_valid_name(name):
	if name == "":
		return False
	else:
		return True

print(is_valid_name("John"))
print(is_valid_name(""))