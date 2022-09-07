## A utility script for quickly putting images into posts

import os
from PIL import Image, ImageDraw, ImageOps, ImageGrab
import numpy as np


DEFAULT_SCREENSHOT_LOCATION = r"C:\Users\lnick\Downloads"


def white_to_transparency_gradient(img):
    x = np.asarray(img.convert('RGBA')).copy()
    x[:, :, 3] &= (255 - x[:, :, :3].min(axis=2)).astype(np.uint8)
    return Image.fromarray(x)


def process(img: Image.Image, save_path: str):

    # make image transparent. Sources:
    # https://stackoverflow.com/questions/71982758/remove-border-from-logo-using-python-pil
    # https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all-white-pixels-transparent
    new_img = white_to_transparency_gradient(img)

    # save the image into the folder
    file_num = 0
    while (filename := f'image-{file_num}.png') in os.listdir(save_path):
        file_num += 1
    else:
        new_img.save(os.path.join(save_path, filename), 'PNG')

    with open(os.path.join(save_path, 'index.md'), 'a') as f:
        f.write(f'![]({filename})\n')

    print(f'Finished processing {filename}!')


if __name__ == '__main__':

    # get image stored in clipboard (Ctrl + C)
    img = ImageGrab.grabclipboard()

    # ask for path to save, containing the `index.md` to be added to
    save_path = os.path.normpath(input('Enter path to output directory: \n'))

    if img is not None:
        print('Image loaded from clipboard')
        process(img, save_path)
    else:
        for filename in filter(lambda s: s.endswith('.png'), os.listdir(DEFAULT_SCREENSHOT_LOCATION)):
            img = Image.open(os.path.join(DEFAULT_SCREENSHOT_LOCATION, filename))
            process(img, save_path)
            os.remove(os.path.join(DEFAULT_SCREENSHOT_LOCATION, filename))
