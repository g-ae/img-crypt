# Launches the decryption process¨
import numpy as np
import matplotlib.image

IMAGE_FILENAME = "image_color.png"

def decrypt():
    to_decrypt = matplotlib.image.imread(IMAGE_FILENAME)
    for (i, line) in enumerate(to_decrypt):
        for (j, pixel) in enumerate(line):
            print(pixel * 255)
            if (j == 3):
                break
        if (i == 1):
            break

if __name__ == "__main__":
    decrypt()
