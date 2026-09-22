\# Current Program Structure



\## cleaner.py



Responsibilities:



* Read command-line arguments
* Open the input CSV file
* Validate CSV headers
* Read CSV rows
* Check empty values
* Check invalid age values
* Detect duplicate rows
* Store valid rows
* Write cleaned CSV output
* Display cleaning results
* Handle missing files
* Handle invalid input



\## cleaning\_functions.py





Reusable functions:



* is\_empty()
* is\_valid\_age()
* is\_duplicate()



\## Current Data Flow



Command line arguments

\-> cleaner.py

\-> Open CSV

\-> Validate headers

\-> Read each row

\-> cleaning\_functions.py

\-> Keep or reject row

\-> Write cleaned CSV

\-> Display result

