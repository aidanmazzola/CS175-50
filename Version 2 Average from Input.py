#CS 175
#Aidan Mazzola
#Average from Input 2



def read_numbers_from_file(file_name):
    numbers = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                try:
                    number = float(line)
                    numbers.append(number)
                except ValueError as ve:
                    print(f"Error converting a value to a number: {ve}")
    except IOError as ioe:
        print(f"Error reading the file: {ioe}")
    return numbers

def calculate_average(numbers):
    if len(numbers) > 0:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    else:
        return None

def main():
    file_name = "numbers.txt"
    numbers = read_numbers_from_file(file_name)

    if numbers:
        for i, number in enumerate(numbers, 1):
            print(f"I read in {i} number(s). Current number is: {number:.2f}")

        average = calculate_average(numbers)
        if average is not None:
            print(f"Average: {average:.1f}")
        else:
            print("No valid numbers were found in the file.")
    else:
        print("No numbers were found in the file.")

if __name__ == "__main__":
    main()
