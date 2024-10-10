'''
COPY PASTED THIS FROM LAST MEETING
MODIFY TO FOLLOW PROJECT STRUCTURE
'''
import numpy as np
from src.util import *
from astropy.io import fits

def median_stack_fits(fits_files: list[Fits], output_file: str):
    # List to store data arrays from FITS files
    image_data = []

    # Read each FITS file and append the data to the list
    for file in fits_files:
        image_data.append(file.get_data())
    
    # Stack the images and compute the median along the stack axis
    stacked_median = np.median(np.array(image_data), axis=0)

    # Create a new FITS HDU (Header/Data Unit) to hold the median image
    hdu = fits.PrimaryHDU(stacked_median)

    # Write the median image to the output FITS file
    hdu.writeto(output_file, overwrite=True)
