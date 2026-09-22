import sys

from csv_utils import read_csv, write_csv
from validators import is_empty, is_valid_age, is_duplicate
from logger_config import logger


def clean_rows(rows):
    cleaned_rows = []
    rejected_rows = 0
    seen_rows = set()

    for row in rows:
        if is_empty(row["name"]) or is_empty(row["email"]):
            print("Rejected row - missing required name or email:", row)
            rejected_rows += 1
            continue

        if not is_valid_age(row["age"]):
            print("Rejected row - age must contain only digits:", row)
            rejected_rows += 1
            continue

        if is_duplicate(row, seen_rows):
            print("Rejected row - duplicate record:", row)
            rejected_rows += 1
            continue

        cleaned_rows.append(row)

    return cleaned_rows, rejected_rows


def run_cleaner(input_file, output_file):
    logger.info("Cleaning started: %s", input_file)

    rows = read_csv(input_file)

    cleaned_rows, rejected_rows = clean_rows(rows)

    write_csv(output_file, cleaned_rows)

    logger.info(
        "Cleaning completed: %d valid rows, %d rejected rows",
        len(cleaned_rows),
        rejected_rows
    )

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
        run_cleaner(input_file, output_file)

    except FileNotFoundError:
        message = f"Input file not found: {input_file}"
        print("Error:", message)
        logger.error(message)

    except ValueError as error:
        print("Error:", error)
        logger.error(str(error))