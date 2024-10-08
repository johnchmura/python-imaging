import sys

from src.module import *  
from src.util import *

# code for main file goes here
def main():
    print(dark_img.darken())
    print(flat_img.flatten())

# run main
if __name__ == "__main__":
    # exec main function
    main()
    sys.exit(0)