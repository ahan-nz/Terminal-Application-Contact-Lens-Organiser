import csv
from datetime import date
import sys
import contactrx

# Get contact lens prescription and assign to variable
try:
    clrx = contactrx.clrx()

    # Print results to terminal, including + or - signs, as per optometry convention
    if clrx >= 0:
        print(f"The contact lens prescription is +{clrx:.2f}DS.")
    else:
        print(f"The contact lens prescription is {clrx:.2f}DS.")

except ValueError:
    print('Please enter a valid Rx in numeric format.')
    sys.exit(1)
except Exception:
    print('Oops! Something went wrong. Try again.')
    sys.exit(1)

# Selecting modality, or wearing schedule, of contact lens
mod = ['daily', 'fortnightly', 'monthly']

print('Please enter the desired contact lens modality:')
for index, item in enumerate(mod):
    print(f"{index+1}. {item}")

# While loop until user enters a valid selection
modality = ''
while modality.lower() not in mod:
    modality = input('Your choice: ')

# Opening selection of contact lenses from external txt file, depending on the modality
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

#close file
f. close()

# User input chosen lens, patient ID and number of lenses needed
lens = input('Enter your choice: ')
id = input('Enter patient ID: ')
amount = input('Enter pairs of lenses needed: ')

# Confirm with user that the details are correct
confirm = input(f"Your order: {amount} pair(s) of {clrx:.2f}DS {lens} lenses, for patient #{id}. Y/N: ")

if confirm.lower() == 'y':
    today = date.today().strftime('%d-%m-%Y')
    order = {'Date': today, 'Patient ID': id, 'Lens': lens, 'CL Rx': clrx, 'Amount (pairs)': amount}
    fields = ['Date', 'Patient ID', 'Lens', 'CL Rx', 'Amount (pairs)']

    # Has this order been placed
    if_ordered = input('Has this order already been placed? Y/N: ')

    # If yes, print to ordered.csv file with today's date
    if if_ordered.lower() == 'y':
        with open('ordered.csv', 'a') as ordered:
            writer = csv.DictWriter(ordered, fieldnames = fields)
            writer.writerow(order)

    # else, print to pending.csv file with today's date
    elif if_ordered.lower() == 'n':
        with open('pending.csv', 'a') as ordered:
            writer = csv.DictWriter(ordered, fieldnames = fields)
            writer.writerow(order)

elif confirm.lower() == 'n':
    pass #loop back to line 1

else:
    print('Please enter \'Y\' or \'N\'')

# Would you like to add another order? 
moreorders = input('Would you like to add another order? Y/N: ')

if moreorders.lower() == 'y':
    pass # return to beginning

# If no, end programme
elif moreorders.lower() == 'n':
    print('Thank you for using our programme.')

else:
    print('Please enter \'Y\' or \'N\'')