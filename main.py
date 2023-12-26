from PIL import Image
from PIL.PngImagePlugin import PngInfo
from math import sqrt, ceil
import os

def get_byte_list(path: str) -> list:
    """
        returns a list of integer representation of bytes in model file
        Arguments:
        name    -- path to model file, must be string
    """
    if not isinstance(path, str):
        raise TypeError('name must be string')
    if not os.path.isfile(path):
        raise ValueError('file not exist')
    
    with open(path, 'rb') as model:
        model = model.read()
    return [b for b in model]

def save_image(path: str):
    """
        returns nothing
        function saves image from model with length of original file in EXIF
        Arguments:
        path    -- path to model file, must be string
    """

    if not isinstance(path, str):
        raise TypeError('path must be string')
    if not os.path.isfile(path):
        raise ValueError('file not exist')

    metadata = {}
    
    with open(path, 'rb') as model:
        raw_data = model.read()
    
    #trying to make square
    width = ceil(sqrt(len(raw_data))) #width of image
    height = ceil(sqrt(len(raw_data))) #height of image
    pixels = width * height #how many pixels are
    raw_data_length = len(raw_data) 
    #saving size of original model in exif of photo
    metadata['length'] = str(raw_data_length)

    #adds 0 to the end since we can full empty space
    while pixels+1 != raw_data_length:
        raw_data += b'x00'
        raw_data_length += 1

    #create and save image in L (grayscale) mode
    #raw_data is pure bytes readed from model
    image = Image.frombuffer('L', (width, height), raw_data)    
    info = PngInfo()
    #adding values from metadata to EXIF (only length but we can also add file extension)
    for key, value in metadata.items():
        info.add_text(key, value)
    image.save('output.png', pnginfo=info)

def read_image(path: str) -> (list, dict):
    """
        return tuple with 2 values:
            list of integer representation of byte
            dict with image EXIF
        Arguments:
        path    -- path to image, must be string
    """
    if not isinstance(path, str):
        raise TypeError('path must be string')
    if not os.path.isfile(path):
        raise ValueError('file not exist')
    
    image = Image.open(path)
    width, height = image.size
    pixels = []
    for y in range(height):
        for x in range(width):
            pixels.append(image.getpixel((x, y)))

    metadata = image.info
    return (pixels, metadata)

def save_model(path: str) -> None:
    """
    function saves model from an image with it.
    returns noting
    Arguments:
        path    -- path to image, must be string
    """
    image, metadata = read_image(path)
    length = int(metadata['length'])
    model_bytes = bytes(image[:length])
    with open('model_from_image.pkl', 'wb') as model:
        model.write(model_bytes)

if __name__ == '__main__':
    model_path: str = 'random_forest_model.pkl'
    image_path: str = 'output.png'

    save_image(model_path)

    save_model(image_path)