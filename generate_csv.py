import random
import csv
import math

def generate_csv():

    # Generate a list of 10,000+ random numbers between 1 and 1,000,000
    numbers = [random.randint(1, 1000000) for _ in range(10000)]

    # Create a CSV file with the first digit distribution following Benford's law
    with open('benford.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number in numbers:
            first_digit = int(str(number)[0])
            writer.writerow([number if first_digit != 1 else random.randint(100, 999)])

    # Create a CSV file with the first digit distribution not following Benford's law
    with open('not_benford.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number in numbers:
            # Generate a random number between 1 and 9 according to a uniform distribution
            first_digit = random.randint(1, 9)

            # Generate a random number with the same first digit as the one we just generated
            # but with the remaining digits being random
            remaining_digits = random.randint(1, 999999)
            number = first_digit * 1000000 + remaining_digits

            writer.writerow([number])

if __name__=="__main__":
    generate_csv()
