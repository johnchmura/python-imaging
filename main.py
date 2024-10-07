from module import dark_img as drk, flat_img as flt
import sys

# code for main file goes here
def main():
    print(drk.darken())
    print(flt.flatten())

# run main
if __name__ == "__main__":
    # exec main function
    main()
    sys.exit(0)