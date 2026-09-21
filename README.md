\# Data Cleaning CLI



\## objective



This project is a Python command-line program that cleans CSV data using reusable functions.



\## Features





* Detect empty required values
* Detect duplicate rows
* Detect invalid age values
* Validates required CSV headers
* Handles missing input files
* Handles empty CSV files
* Save cleaned data into a new CSV file



\## Required CSV Columns



The input CSV must contain:



* name
* email
* age



\## How to Run



python src/cleaner.py data/messy\_data.csv output/cleaned\_data.csv



\## Data Flow





CSV input

\-> Read each row

\-> Check required headers

\-> Check empty values

\-> Validate age

\-> Check duplicates

\-> Keep valid rows

\-> Save cleaned CSV output



\## Example Input



name,email,age

John,John@email.com,25

Sarah,sarah@gmail.com,22

,missing@gmail.com,30

David,david@gmail.com,abc

John,John@email.com,25

Emily,,28

Michael,michael@gmail.com,35



\## Example Output



name,email,age

John,John@gmail.com,25

Sarah,sarah@gmail.com,22

Michael,michael@gmail.com,35



\## Error Handling



The CLI handles:



* Missing input files
* Empty CSV files
* Missing required columns
* Empty name or email values
* Invalid age values
* Duplicate rows



\## Reusable Functions 



\### is\_empty()



checks whether a required value is empty.



\### is\_duplicate()



Checks whether the same row has already appeared in the dataset.

