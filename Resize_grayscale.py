from PIL import Image
import numpy as np
from io import BytesIO
import requests as rq

def shape_grey(image):
    img = image.convert('L')
    new_width = 256
    new_height = 256
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return list(np.array(img))
def main(pictures):
    for picture in pictures:
        image = rq.get(picture.thumbnail_url)
        image = Image.open(BytesIO(image.content))
        picture.pixel_array = shape_grey(image)
    return pictures

if __name__ == '__main__':
    main()