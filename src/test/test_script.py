# tests can go here, or not doesn't really matter

def test_Fits():
    from src.util import Fits
    from src.util import Constant
    
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

    # check FITS object is assigned to a path
    one.fits_set(Constant.DARK_PATH + "dark_3_000_1681706756.fits")
    assert one.hdul != None

    # check FITS image type
    print(one.fits_type())
    assert one.fits_type() != None
    
    print(two.fits_type())
    assert two.fits_type() != None


if __name__ == "__main__":
    test_Fits()