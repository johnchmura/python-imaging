def darken():
    return f"darken!"


'''
COPY PASTED THIS FROM LAST MEETING
MODIFY TO FOLLOW PROJECT STRUCTURE
'''
import numpy as np
from astropy.io import fits
import os

def is_dark_image(fits_file):
    """
    Check if the FITS file has 'OBJECT' header with value 'dark'.
    """
    with fits.open(fits_file) as hdul:
        header = hdul[0].header
        return header.get('OBJECT', '').lower() == 'dark'

def median_stack_fits(fits_dir, output_file):
    """
    Stack the median of all dark images from a directory of FITS files.
    
    Parameters:
    - fits_dir: Directory containing FITS files
    - output_file: Path for the output median stacked FITS file
    """
    # List to store data arrays from FITS files that match the 'dark' header
    dark_image_data = []

    # Loop over all files in the input
    for file_name in os.listdir(fits_dir):
        file_path = os.path.join(fits_dir, file_name)
        
        # Check if it's a FITS file and if it's a dark image
        if file_name.endswith('.fits') and is_dark_image(file_path):
            with fits.open(file_path) as hdul:
                # Append the image data to the list if the file is dark
                dark_image_data.append(hdul[0].data)

    if len(dark_image_data) == 0:
        raise ValueError("No dark images found in the directory.")

    # Stack the images and compute the median along the stack axis
    stacked_median = np.median(np.array(dark_image_data), axis=0)

    # Create a new FITS HDU (Header/Data Unit) to hold the median image
    hdu = fits.PrimaryHDU(stacked_median)

    # Write the median image to the output FITS file
    hdu.writeto(output_file, overwrite=True)


fits_dir = 'resource/input/'  # Directory containing FITS files
output_file = 'resource/output/median_stack_dark.fits'

median_stack_fits(fits_dir, output_file)
