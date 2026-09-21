# Week 2 - Reusable Data Cleaning Functions


seen_rows = set()

def is_empty(value):

	if value == "":
		return True

	else:
		return False

def is_valid_age(age):
	if age.isdigit():
		return True
	else:
		return False

def is_duplicate(row):
	row_key = tuple(row.items())

	if row_key in seen_rows:
		return True

	seen_rows.add(row_key)
	return False

# Test the functions only when this file is run directly
if __name__ == "__main__":
	print("Testing is_empty():")
	print(is_empty(""))
	print(is_empty("John"))

	print("--------------------")

	print("Testing is_valid_age():")
	print(is_valid_age("25"))
	print(is_valid_age("abc"))
	print(is_valid_age(""))

	print("--------------------")

	row1 = {
		"name": "John",
		"email": "john@gmail.com",
		"age": "25"
	}
	
	row2 = {
		"name": "Sarah",
		"email": "john@email.com",
		"age": "22"
	}

	row3 = {
		"name": "John",
		"email": "john@gmail.com",
		"age": "25"
	}

	print("Testing is_duplicate():")
	print(is_duplicate(row1))
	print(is_duplicate(row2))
	print(is_duplicate(row3))