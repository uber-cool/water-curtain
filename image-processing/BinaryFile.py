from PIL import Image
import numpy as np


def get_binary_file(file_path, target_file_path):
    src_image = Image.open(file_path)
    gray_image = src_image.convert('L')

    array = np.array(gray_image)
    np.savetxt(target_file_path, array < 128, fmt="%d")