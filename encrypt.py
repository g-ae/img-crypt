import numpy as np  # Black image creation (array of arrays of zeros)
import matplotlib.image

# Image will be saved as a PNG to avoid compression issues that come with JPEG
IMAGE_FILENAME = "DEFAULT_IMAGE.png"

# Main encryption function
def encrypt():
    # Width and height of the target image
    WIDTH = 1000
    HEIGHT = 1000
    # Create an array of zeros (black image) with the right size
    final = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    # v0.1 = up to 1million chars (WIDTH * HEIGHT) -> test values
    to_encypt = """Lorem ipsumaaaas dolor sit amet, consectetur adipiscing elit. Donec auctor, nisl eget tincidunt lacinia, nisl nisl aliquam, eget aliquam nisl nisl eu nisl. Donec a"""
    # if char > 255 * 3, it will be replaced by a question mark -> too high to be placed in a colored pixel -> could maybe be improved with alpha ???
    OUT_OF_BOUNDS = ord('?')

    # Indexes
    current_line = 0
    current_column = 0

    # For each character in the encryption string
    for (i, char) in enumerate(to_encypt):
        if ord(char) > 255 * 3:
            # If the character is out of bounds, replace it by a question mark
            final[current_line][current_column] = [OUT_OF_BOUNDS, 0, 0]
        else:
            # Else, place the character in the image using BGR values
            b = 0
            g = 0
            r = 0
            if ord(char) > 0 and ord(char) < 256:
                # 0-255 -> place only in blue
                b = ord(char)
            elif ord(char) >= 256 and ord(char) < 255 + 255:
                # 256-511 -> place in green and blue
                b = 255
                g = ord(char) - 255
            else:
                # 512-767 -> place in all colors
                b = 255
                g = 255
                r = ord(char) - 255 - 255
            # Add wanted color to the pixel
            final[current_line][current_column] = [b, g, r]

        # Next line
        if current_column == WIDTH -1:
            current_line += 1
            current_column = 0
        
        # If 1 million characters reached, stop
        if current_line == HEIGHT:
            print("1 million characters reached")
            break

        # Index
        current_column += 1

    # Save the image
    matplotlib.image.imsave(IMAGE_FILENAME, final)

if __name__ == "__main__":
    encrypt()