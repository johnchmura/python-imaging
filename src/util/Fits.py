from astropy.io import fits
from src.util.Constant import *
import os

'''
Class to handle FITS files

Current implementation opens FITS header upon initialization 
to avoid repeated access which in turn improves performance, 
assuming memory is of no concern. Otherwise, change class to 
implement lazy-loading.
'''
class Fits:
    def __init__(self, path: str = None):
        self.path = None
        self.hdul = None

        # by default, set is_output flag to True 
        # (if path is not a FITS file, it is for output)
        if (path):
            self.fits_set(path, True)

    '''
    Retrieve the FITS image's type. 
    @return str: Image type of FITS object

    TODO:   Take into account different standards of storing 
            image type, not always the case it's in "TARGET"
    '''
    def fits_type(self) -> str:
            return self.hdul[0].header[Constant.HeaderObj.TYPE_KEY]
    
    '''
    Set the object's FITS path
    @arg path:      String of file path to FITS file
    @arg is_output: Flag for setting FITS output
    '''
    def fits_set(self, path: str, is_output: bool = False):
        # if given path points to existing FITS file, open HDUL
        if (self.fits_path_check(path)):
            self.path = path
            self.hdul = fits.open(path)
        elif is_output:
            self.path = path
            self.hdul = None
        else:
            raise FileNotFoundError(f"Provided path {path} is not a FITS file")

    '''
    Helper function to see header info. From what I understand,
    a FITS file can have multiple image data. Typically if we
    are looking for only the primary data it should be on index
    zero, the rest is irrelevant.
    '''
    def fits_hdul_info(self):
        self.hdul.info()

    '''
    Retrieve data from selected HDU
    @arg index:     The index of the HDU from which data is to
                    be pulled from. Default is 0 (primary HDU)
    @return lst:    The data from the selected HDU
    '''
    def get_data(self, index: int = 0) -> list:
        if (index < 0):
            raise IndexError("Invalid negative index")
        return self.hdul[index].data
        
    '''
    Method to check image type without making FITS object
    @arg path: Complete path to FITS file
    '''
    @staticmethod
    def check_type(path: str) -> str:
        return fits.open(path)[0].header[Constant.HeaderObj.TYPE_KEY]

    '''
    Static method to check if given path is valid FITS file
    @arg path:      String of file path to FITS file
    @return bool:   True if given path points to an existing 
                    Fits file, false otherwise
    '''
    @staticmethod
    def fits_path_check(path: str) -> bool:
        if os.path.isfile(path) and path.endswith('.fits'):
            return True
        return False

    '''
    Creates FITS object for every image found in given 
    directory and return a list of FITS objects
    @arg path:  Path to directory with FITS images
    @arg type:  Type of images to collect
    @return:    List of FITS objects
    '''
    @staticmethod
    def batch_fits(path: str, type: str):
        fits_list = []

        if (os.path.isdir(path)):
            for files in os.listdir(path):
                # find FITS with specified type
                if (Fits.fits_path_check(path + files) and type == Fits.check_type(path + files)):
                    fits_list.append(Fits(path + files))
           
            return fits_list
        else:
            raise NotADirectoryError(f"Provided path {path} is not a directory")