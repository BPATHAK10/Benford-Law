# Benford's Law Checker

## Introduction

This is a web application built using the Pyramid web framework in Python. The application has one endpoint at `/benford` which accepts a CSV file with just one column and at least 10,000 rows of numbers as input. The application checks if the input CSV conforms to Benford's Law on the first digits and produces a JSON output indicating the results.

## Technologies Used

- Python
- Pyramid web framework
- Pandas
- NumPy
- Matplotlib
- JSON

## Installation

1. Clone the project repository.
2. Create a virtual environment for the project using Python.
3. Activate the virtual environment.
4. Install the required packages using pip and the requirements.txt file: `pip install -r requirements.txt`
5. Run the application using the command `python app.py development.ini` in the project directory.
6. Access the application in your web browser at `http://localhost:6543/`.
7. Upload the CSV file to check the Benford's Law and obtain the results.

## Usage

1. Upload a CSV file with just one column and at least 10,000 rows of numbers to the `/benford` endpoint.
2. The application will check if the input CSV conforms to Benford's Law on the first digits.
3. The application will produce a JSON output indicating whether the input CSV conforms to Benford's Law and a plot of the distribution of first digits in the input CSV.
4. If the input CSV conforms to Benford's Law, the JSON output will indicate that the input data conforms and the plot will show the expected distribution of first digits as a red dashed line and the observed distribution of first digits in the input data as blue bars.
5. If the input CSV does not conform to Benford's Law, the JSON output will indicate that the input data does not conform and the plot will show the same as above.
