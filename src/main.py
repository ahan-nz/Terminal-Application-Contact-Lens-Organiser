import csv
from datetime import date

# Calculate contact lens prescription, and round result to nearest 0.25 dioptre steps as per optometry convention
def clrx():
   return round((rx / (1 - ((d/1000) * rx))) * 4)/4

# Get user input for spectacle prescription (Rx) and back vertex distance (BVD)
rx = float(input('Enter spherical Rx (DS): '))
d = float(input('Enter back vertex distance (mm): '))

clrx = clrx()
# Print results, including + or - signs, as per optometry convention
if clrx >= 0:
    print(f"The contact lens prescription is +{clrx:.2f}DS.")
else:
    print(f"The contact lens prescription is {clrx:.2f}DS.")

# Selecting type of contact lens
mod = ['daily', 'fortnightly', 'monthly']

print('Please enter the desired contact lens modality:')
for index, item in enumerate(mod):
    print(f"{index+1}. {item}")

modality = ''
while modality.lower() not in mod:
    modality = input('Your choice: ')

# Selecting the lens desired

print('Please choose from the following lenses: ')

if modality.lower() == 'daily':
    f = open('daily.txt')
        
elif modality.lower() == 'fortnightly':
    f = open('fortnightly.txt')

elif modality.lower() == 'monthly':
    f = open('monthly.txt')

for line in f:
    print(f'{line.strip()}')

lens = input('Your choice: ')

f. close()

id = input('Enter patient ID: ')
amount = input('Enter pairs of lenses needed: ')

confirm = input(f"Your order: {amount} pair(s) of {clrx:.2f}DS {lens} lenses, for patient #{id}. Y/N: ")
if confirm.lower() == 'y' or 'yes':
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


else:
    pass #loop back to line 1


# Would you like to add another order? 
# If yes, return to beginning
# If no, end programme.