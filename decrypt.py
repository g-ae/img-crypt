# Launches the decryption process
import matplotlib.image # pip install matplotlib - read image (pixel by pixel)

IMAGE_FILENAME = "DEFAULT_IMAGE.png"  # Base target image (will be changed in the future)
final=""        # Final decrypted message
ended = False   # If the decryption is finished

# Main decryption function
def decrypt():
    # Global variables
    global ended
    global final

    # Read the image
    to_decrypt = matplotlib.image.imread(IMAGE_FILENAME)
    # For each line
    for (i, line) in enumerate(to_decrypt):
        # If the decryption is not finished
        if not ended:
            # For each pixel (column)
            for (j, pixel) in enumerate(line):
                # If the pixel is black, the decryption is finished
                if pixel[0] == 0:
                    print("Finished")
                    ended = True
                    break
                # Add character to the final message
                final += chr(int(pixel[0] * 255) + int(pixel[1] * 255) + int(pixel[2] * 255))
    # At the end, print the decryted message
    print("Decrypted message :" + chr(10) + final)
        

if __name__ == "__main__":
    decrypt()
