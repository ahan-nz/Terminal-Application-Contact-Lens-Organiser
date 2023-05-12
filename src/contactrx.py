# Calculate contact lens prescription from known clinical measurements

def clrx():
   # Get user input for spectacle prescription (Rx) and back vertex distance (BVD)
    rx = float(input('Enter spherical Rx (DS): '))
    d = float(input('Enter back vertex distance (mm): '))
    # Round result to nearest 0.25 dioptre steps as per optometry convention
    return round((rx / (1 - ((d/1000) * rx))) * 4)/4