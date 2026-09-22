# validation functions for the data-cleaning CLI

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

def is_duplicate(row, seen_rows):
	row_key = tuple(row.items())

	if row_key in seen_rows:
		return True
	
	seen_rows.add(row_key)
	return False