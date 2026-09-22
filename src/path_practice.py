from pathlib import Path

input_file = Path("data/messy_data.csv")

print("File path:", input_file)
print("File exists:", input_file.exists())
print("File name:", input_file.name)
print("Parent folder:", input_file.parent)