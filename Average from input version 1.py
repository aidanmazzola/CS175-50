#CS175
#Aidan Mazzola
#Average From Input

# Open the file for reading
with open("numbers.txt", "r") as file:
    total = 0
    count = 0

    for line in file:
        number = float(line)
        count += 1
        total += number
        print(f"I read in {count} number(s) Current number is: {number:.2f} Total is: {total:.2f}")

# Calculate the average
if count > 0:
    average = total / count
    print(f"Average: {average:.1f}")
else:
    print("No numbers were found in the file.")

    
