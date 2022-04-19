import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps


def run():
    path = Path(sys.argv[1])

    image = Image.open(path)
    data = image.getdata()

    basename, extension = os.path.splitext(path)

    red = [(d[0], 0, 0) for d in data]
    red_image = image.copy()
    red_image.putdata(red)

    green = [(0, d[1], 0) for d in data]
    green_image = image.copy()
    green_image.putdata(green)

    blue = [(0, 0, d[2]) for d in data]
    blue_image = image.copy()
    blue_image.putdata(blue)

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
