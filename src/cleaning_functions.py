# Week 2 - Data Cleaning Functions

def is_empty(value):
	if value == "":
		return True
	else:
		return False

print(is_empty(""))
print(is_empty("John"))

print("--------------------")

def is_valid_age(age):
	if age.isdigit():
		return True
	else:
		return False

print(is_valid_age("25"))
print(is_valid_age("abc"))
print(is_valid_age(""))

print("--------------------")

seen_rows = set()

def is_duplicate(row):
	row_key = tuple(row.items())

	if row_key in seen_rows:
		return True

	seen_rows.add(row_key)
	return False


row1 = {
	"name": "John",
	"email": "john@gmail.com",
	"age": "25"
}

row2 = {
	"name": "Sarah",
	"email": "sarah@gmail.com",
	"age": "22"
}

row3 = {
	"name": "John",
	"email": "john@gmail.com",
	"age": "25"
}

print(is_duplicate(row1))
print(is_duplicate(row2))
print(is_duplicate(row3))
