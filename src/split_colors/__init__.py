import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps


def run():
    path = Path(sys.argv[1])

    image = Image.open(path)

    basename, extension = os.path.splitext(path)

    red = np.asarray(image.getchannel("R"))
    red_image = ImageOps.colorize(Image.fromarray(red, "L"), "#FF0000", "#FFFFFF")

    green = np.asarray(image.getchannel("G"))
    green_image = ImageOps.colorize(Image.fromarray(green, "L"), "#00FF00", "#FFFFFF")

    blue = np.asarray(image.getchannel("B"))
    blue_image = ImageOps.colorize(Image.fromarray(blue, "L"), "#0000FF", "#FFFFFF")

    try:
        alpha = image.getchannel("A")
        red_image.putalpha(alpha)
        green_image.putalpha(alpha)
        blue_image.putalpha(alpha)
    except ValueError:
        # No alpha channel
        pass

    red_image.save(f"{basename}-red{extension}")
    green_image.save(f"{basename}-green{extension}")
    blue_image.save(f"{basename}-blue{extension}")


if __name__ == "__main__":
    run()
