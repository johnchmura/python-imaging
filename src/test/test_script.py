# tests can go here, or not doesn't really matter
from src.module import *
from src.util import *

def test_Fits():
    # check constructor called with no path
    one = Fits()
    assert one.hdul == None

    # check path validator function
    assert Fits.fits_path_check(r"C:\Users\bloon\Desktop\python-imaging\resource\dark_images\dark_3_000_1681706713.fits") == True
    assert Fits.fits_path_check(Constant.DARK_PATH) == False
    assert Fits.fits_path_check(Constant.DARK_PATH + "dark_3_000_1681706713.fits") == True

    # check constructor called with valid path
    two = Fits(Constant.DARK_PATH + "dark_3_000_1681706713.fits")
    assert two.hdul != None

    # check constructor called with non-existing FITS file
    three = Fits(Constant.OUTPUT_PATH + "output.fits")
    assert three.hdul == None
    print(three.path)
    assert three.path == Constant.OUTPUT_PATH + "output.fits"

    # assign FITS object to output path
    one.fits_set(Constant.OUTPUT_PATH + "output.fits", True)
    assert one.hdul == None
    print(one.path)
    assert one.path == Constant.OUTPUT_PATH + "output.fits"

    # check FITS object is assigned to a path
    one.fits_set(Constant.DARK_PATH + "dark_3_000_1681706756.fits")
    assert one.hdul != None

    # check FITS image type
    print(one.fits_type())
    assert one.fits_type() != None
    
    print(two.fits_type())
    assert two.fits_type() != None

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
    output_file = Constant.OUTPUT_PATH + "output.fits" # or change this to a path

    median_stack_fits(fits_files, output_file)

if __name__ == "__main__":
    #test_Fits()
    test_dark_img()