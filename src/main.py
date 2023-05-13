import csv
from datetime import date
import sys
import enum
import contactrx

print('\nWelcome to Alicia\'s contact lens ordering programme, made for optometrists and clinic staff.\n')

def exception():
    print('Oops! Something went wrong. Please try again.')
    sys.exit(1)

# Get contact lens prescription and assign to variable
while True:
    try:
        clrx = contactrx.clrx()

        # Print results to terminal, including + or - signs, as per optometry convention
        if clrx >= 0:
            print(f"The contact lens prescription required is +{clrx:.2f}DS.")
            break
        else:
            print(f"The contact lens prescription required is {clrx:.2f}DS.")
            break

    # Error handling for input parameters
    except ValueError:
        print('Please enter a valid input in numeric format.')
        continue
    except Exception:
        exception()

# Selecting modality, or wearing schedule, of contact lens
mod = ['daily', 'fortnightly', 'monthly']

print('Please enter the desired contact lens modality:')
for index, item in enumerate(mod):
    print(f"{index+1}. {item}")

# While loop until user enters a valid selection
while True:
        modality = input('Your choice: ')

        if modality in mod:
            break
        
        else:
            print('Invalid selection, please choose from \'daily\', \'fortnightly\', or \'monthly\'.')

# Opening selection of contact lenses from external txt file, depending on the modality
def open_list():
    print('Please choose from the following lenses: ')

    if modality.lower() == 'daily':
        f = open('daily.txt')
            
    elif modality.lower() == 'fortnightly':
        f = open('fortnightly.txt')

    elif modality.lower() == 'monthly':
        f = open('monthly.txt')

    # Printing list of available contact lenses to terminal
    for line in f:
            print(f'{line.strip()}')

    # Close txt file
    f. close()

open_list()

def invalid_choices():
    print('Too many invalid choices, programme ending.')
    sys.exit(1)

# User input chosen lens, patient ID and number of lenses needed
lens = input('Enter your choice, or specify another lens: ')
id = input('Enter patient ID: ')

while True:
    try:
        amount = int(input('Enter pairs of lenses needed: '))

        if amount >= 1:
            break
            
        else:
            print('Amount can\'t be less than 1!')

    except ValueError:
        print('Value entered wasn\'t an integer.')
        continue

    except Exception:
        exception()

def y_or_n():
    print('Please enter \'Y\' or \'N\'.')

for retry in range(5):
    # Confirm with user that the details are correct
    confirm = input(f"Your order: {amount} pair(s) of {clrx:.2f}DS {lens} lenses, for patient #{id}. Y/N: ")

    if confirm.lower() == 'y':
        today = date.today().strftime('%d-%m-%Y')
        order = {'Date': today, 'Patient ID': id, 'Modality': modality, 'Lens': lens, 'CL Rx': clrx, 'Amount (pairs)': amount}
        fields = ['Date', 'Patient ID', 'Modality', 'Lens', 'CL Rx', 'Amount (pairs)']

        for retry in range(5):
            # Has this order been placed
            if_ordered = input('Has this order already been placed? Y/N: ')

            # If yes, print to ordered.csv file with today's date
            if if_ordered.lower() == 'y':
                with open('ordered.csv', 'a') as ordered:
                    writer = csv.DictWriter(ordered, fieldnames = fields)
                    writer.writerow(order)
                break

            # else, print to pending.csv file with today's date
            elif if_ordered.lower() == 'n':
                with open('pending.csv', 'a') as ordered:
                    writer = csv.DictWriter(ordered, fieldnames = fields)
                    writer.writerow(order)
                break
                    
            else:
                y_or_n()

        else:
            invalid_choices()

        break

    elif confirm.lower() == 'n':
        print('Please start again.')
        sys.exit(1)

    else:
        y_or_n()

else:
    invalid_choices()

def read_ordered_lenses():
    print('The following orders have been placed:')
    with open('ordered.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

def read_pending_lenses():
    print('The following orders are pending:')
    with open('pending.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

while True:
    history = input('Would you like to see previous order details? Y/N: ')

    if history.lower() == 'y':
        read_ordered_lenses()
        read_pending_lenses()
        break

    elif history.lower() == 'n':
        break

    else:
        y_or_n()

print('\nThank you for using this programme!\n')