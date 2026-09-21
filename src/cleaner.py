import csv
import sys

from cleaning_functions import is_empty, is_valid_age, is_duplicate


def clean_csv(input_file, output_file):
    cleaned_rows = []
    rejected_rows = 0

    with open(input_file, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError(
                "Input CSV is empty or does not contain a header."
            )

        required_headers = ["name", "email", "age"]

        for header in required_headers:
            if header not in reader.fieldnames:
                raise ValueError(
                    f"Missing required column: {header}"
                )

        for row in reader:
            if is_empty(row["name"]) or is_empty(row["email"]):
                print("Rejected - empty value:", row)
                rejected_rows += 1
                continue

            if not is_valid_age(row["age"]):
                print("Rejected - invalid age:", row)
                rejected_rows += 1
                continue

            if is_duplicate(row):
                print("Rejected - duplicate:", row)
                rejected_rows += 1
                continue

            cleaned_rows.append(row)

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:
        fieldnames = ["name", "email", "age"]

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(cleaned_rows)

    print("--------------------")
    print("Cleaning completed.")
    print("Valid rows:", len(cleaned_rows))
    print("Rejected rows:", rejected_rows)
    print("Output file:", output_file)


if len(sys.argv) != 3:
    print(
        "Usage: python src/cleaner.py "
        "<input.csv> <output.csv>"
    )
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        clean_csv(input_file, output_file)

    except FileNotFoundError:
        print(
            "Error: Input file not found:",
            input_file
        )

    except ValueError as error:
        print("Error:", error)