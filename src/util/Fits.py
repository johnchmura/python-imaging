from astropy.io import fits
from src.util.Constant import *
import os

'''
Class to handle FITS files
'''
class Fits:
    def __init__(self, path: str = None):
        self.path = None
        self.hdul = None

        if (path):
            self.fits_set(path)


    '''
    Retrieve the FITS image's type. 
    @return str: Image type of FITS object
    
    TODO
    Might wanna take into account the different standards the 
    images use, not always the case the key happens to be "TARGET"
    '''
    def fits_type(self) -> str:
            return self.hdul[0].header["TARGET"]
    

    '''
    Set the object's FITS path
    @argument: String of file path to FITS file
    '''
    def fits_set(self, path: str):
        # if given path points to existing FITS file, open HDUL
        if (self.fits_path_check(path)):
            self.path = path
            self.hdul = fits.open(path)
        else:
            # assume path is to write new FITS file
            self.path = path
            self.hdul = None


    '''
    Static method to check if given path is valid FITS file
    @argument path: String of file path to FITS file
    @return bool:   True if given path points to an existing 
                    Fits file, false otherwise
    '''
    @staticmethod
    def fits_path_check(path: str) -> bool:
        if os.path.isfile(path) and path.endswith('.fits'):
            return True
        return False
    