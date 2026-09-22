import csv

from pathlib import Path


REQUIRED_HEADERS = ["name", "email", "age"]


def read_csv(input_file):
    with open(input_file, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError(
                "Input CSV is empty or does not contain a header."
            )

        for header in REQUIRED_HEADERS:
            if header not in reader.fieldnames:
                raise ValueError(
                    f"Missing required column: {header}"
                )

        return list(reader)


def write_csv(output_file, rows):
    output_path = Path(output_file)
    
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=REQUIRED_HEADERS
        )

        writer.writeheader()
        writer.writerows(rows)