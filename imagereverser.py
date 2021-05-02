# importing os module
import os

files = []
directoryname = "output_reversesequence"
# directoryname = "test"


def main():
    print("\n")

    # put all the filenames in an array called "files"
    for (filenames) in os.walk(directoryname):
        for filename in filenames:
            filename = sorted(filename)
            files = filename

    files.pop(0)  # cut out .ds_store bullshit
    print(files)

    print(f"number of files is {len(files)}")
    # get the number for the last image in the sequence
    pivotnumber = int(files[-1].replace(".png", ""))
    print(f"Pivot around {pivotnumber}")

    files.pop()  # remove the last image, since we don't want a duplicate frame
    sequencelength = len(files)
    print(
        f"the number of images to reverse is {sequencelength} \n")

    for file in files:

        print(f"starting file name is {file}")
        filestring = file.replace(".png", "")
        filenumber = int(filestring)
        print(f"the number in the sequence is {filenumber}")
        reversednumber = (pivotnumber - filenumber) + pivotnumber
        print(f"the number should be {reversednumber}")
        new_filename = str(reversednumber) + ".png"
        print(f"the new filename should be {new_filename}")

        os.rename(f"{directoryname}/{file}", f"{directoryname}/{new_filename}")
        print(f"\nSuccessfully renamed {file} to {new_filename}")

        print("\n")


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
