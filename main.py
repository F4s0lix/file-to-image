import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from math import sqrt, ceil

def get_byte_list(name: str) -> list:
    with open(name, 'rb') as model:
        model = model.read()
    return [b for b in model]

def save_image(name: str):
    with open(name, 'rb') as model:
        raw_data = model.read()
    #trying to make square
    width = ceil(sqrt(len(raw_data)))
    height = ceil(sqrt(len(raw_data)))
    pixels = width * height
    raw_data_length = len(raw_data)
    #adds 0 to the end since we can full empty space
    while pixels+1 != raw_data_length:
        raw_data += b'x00'
        raw_data_length += 1
    #create and save image in L (grayscale) mode
    image = Image.frombuffer('L', (width, height), raw_data)
    
    metadata = image.info
    metadata['length'] = str(raw_data_length)
    print(metadata)
    image.save('blagam.png')

def read_image(path: str):
    image = Image.open(path)
    width, height = image.size
    pixels = []
    for y in range(height):
        for x in range(width):
            pixels.append(image.getpixel((x, y)))

    length = image.info
    print(length)
    return (pixels, length)

name: str = 'random_forest_model.pkl'
image: str = 'blagam.png'

save_image(name)

obraz, length = read_image(image)
model = get_byte_list(name)


print(obraz[0:length] == model)