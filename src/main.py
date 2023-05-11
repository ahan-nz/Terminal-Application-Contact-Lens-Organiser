# Get user input for spectacle prescription (Rx) and back vertex distance (BVD)
rx = float(input('Enter spherical Rx (DS): '))
d = float(input('Enter back vertex distance (mm): '))

def clrx(rx, d):
    # Calculate contact lens prescription, and round result to nearest 0.25 dioptre steps as per optometry convention
   return round((rx / (1 - ((d/1000) * rx))) * 4)/4

clrx = clrx(rx, d)

# Print results, including + or - signs, as per optometry convention
if clrx >= 0:
    print(f"The contact lens prescription is +{clrx:.2f}DS.")
else:
    print(f"The contact lens prescription is {clrx:.2f}DS.")
