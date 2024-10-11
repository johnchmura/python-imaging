# tests can go here, or not doesn't really matter
from src.module import *
from src.util import *

def test_Fits():
    # check HDUL info function
    # two.fits_hdul_info()

    # check get_data from FITS object
    # print(two.get_data())

    # check batch loading FITS
    for files in (Fits.batch_fits(Constant.DARK_PATH, Constant.HeaderObj.DARK_IMG)):
        print(files.path)


# ngetes dark_img
def test_dark_img():
    fits_files = Fits.batch_fits(Constant.DARK_PATH, Constant.HeaderObj.DARK_IMG)
    output_file = Constant.OUTPUT_PATH + "ngentot_gasih.fits" # or change this to a path

    master_dark = median_stack_fits(fits_files, output_file)
    # tulis ke kaset
    master_dark.write_to_disk(True)

if __name__ == "__main__":
    # test_Fits()
    test_dark_img()