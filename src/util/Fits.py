from astropy.io import fits
from src.util.Constant import *
import os, re


'''
Class to handle FITS files
'''
class Fits:
    def __init__(self, path: str = None):
        self.hdul = None

        if (path):
            self.fits_set(path)


    '''
    Retrieve the FITS image's type. 
    @return str: Image type of FITS object
    
    TODO: Might wanna take into account the different standards the 
    images use, not always the case the key happens to be "TARGET"
    '''
    def fits_type(self) -> str:
        return self.hdul[0].header["TARGET"]


    '''
    Set the object's FITS path
    @argument: String of file path to FITS file
    '''
    def fits_set(self, path: str):
        if (self.fits_path_check(path)):
            self.hdul = fits.open(path)
        else:
            raise Exception("Invalid path to FITS file")


    '''
    Static method to check if given path is valid FITS file with regex
    @argument path: String of file path to FITS file
    @return bool:   True if given path points to an existing Fits file, 
                    false otherwise
    '''
    @staticmethod
    def fits_path_check(path: str) -> bool:
        if os.path.isfile(path) and re.match(r"^.*\.fits$", path):
            return True
        return False
    