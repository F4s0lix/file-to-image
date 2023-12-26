from PIL import Image
from PIL.PngImagePlugin import PngInfo
from math import sqrt, ceil

def get_byte_list(name: str) -> list:
    with open(name, 'rb') as model:
        model = model.read()
    return [b for b in model]

def save_image(name: str):
    metadata = {}
    
    with open(name, 'rb') as model:
        raw_data = model.read()
    
    #trying to make square
    width = ceil(sqrt(len(raw_data)))
    height = ceil(sqrt(len(raw_data)))
    pixels = width * height
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

if __name__ == '__main__':
    name: str = 'random_forest_model.pkl'
    image: str = 'protonmail-asimage.png'

    save_image(name)

    obraz, metadata = read_image(image)
    length = int(metadata['length'])
    model = get_byte_list(name)
    print(obraz[:1704753] == model)