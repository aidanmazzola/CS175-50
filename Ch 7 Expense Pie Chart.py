#CS 175
#Aidan Mazzola
#Expense pie chart

import matplotlib.pyplot as plt

def read_expenses(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                label, value = line.strip().split('\t')
                data.append((label, int(value)))
    except IOError:
        print("Error: Unable to open the file.")
    except ValueError:
        print("Error: Data conversion error. Check the format of the file.")
    return data

def create_pie_chart(data):
    labels, values = zip(*data)
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Expense Distribution")
    plt.show()

def main():
    file_path = 'expenses.txt'
    expenses_data = read_expenses(file_path)
    
    if expenses_data:
        create_pie_chart(expenses_data)

if __name__ == "__main__":
    main()
