def darken():
    return f"darken!"


'''
COPY PASTED THIS FROM LAST MEETING
MODIFY TO FOLLOW PROJECT STRUCTURE
'''
import numpy as np
from astropy.io import fits

def median_stack_fits(fits_files, output_file):
    # List to store data arrays from FITS files
    image_data = []

    # Read each FITS file and append the data to the list
    for file in fits_files:
        with fits.open(file) as hdul:
            # Get the image data (assuming it's in the primary HDU)
            image_data.append(hdul[0].data)
    
    # Stack the images and compute the median along the stack axis
    stacked_median = np.median(np.array(image_data), axis=0)

    # Create a new FITS HDU (Header/Data Unit) to hold the median image
    hdu = fits.PrimaryHDU(stacked_median)

    # Write the median image to the output FITS file
    hdu.writeto(output_file, overwrite=True)

# Example usage -- change this to get files from a path and then create a new function to check for the headers and see if OBJECT = dark
fits_files = [
    '/example1.fits',
    '/example2.fits',
    '/example3.fits'
]
output_file = '/median_stack.fits' # or change this to a path

median_stack_fits(fits_files, output_file)