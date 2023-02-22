import numpy as np
import matplotlib.image

IMAGE_FILENAME = "image_color.png"

def encrypt():
    WIDTH = 1000
    HEIGHT = 1000
    final = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    # v0.1 = up to 1million chars
    to_encypt = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, nisl eget tincidunt lacinia, nisl nisl aliquam, eget aliquam nisl nisl eu nisl. Donec a"""
    OUT_OF_BOUNDS = ord('?')
    current_line = 0
    current_column = 0

    for (i, char) in enumerate(to_encypt):
        if ord(char) > 255 * 3:
            final[current_line][current_column] = [OUT_OF_BOUNDS, 0, 0]
        else:
            b = 0
            g = 0
            r = 0
            if ord(char) > 0 and ord(char) < 256:
                # 0-255
                b = ord(char)
            elif ord(char) >= 256 and ord(char) < 255 + 255:
                # 256-511
                g = ord(char) - 255
            else:
                # 512-767
                r = ord(char) - 255 - 255
            final[current_line][current_column] = [b, g, r]

        # Next line
        if current_column == WIDTH -1:
            current_line += 1
            current_column = 0
        if current_line == HEIGHT:
            print("1 million characters reached")
            break

        # Column
        current_column += 1

    matplotlib.image.imsave(IMAGE_FILENAME, final)

if __name__ == "__main__":
    encrypt()