import os
import filetype
from PIL import Image
from constants import *


def gray_scale(pixel):
    if isinstance(pixel, int):
        # Pixel is already grayscale
        return pixel
    else:
        return RED * pixel[0] + GREEN * pixel[1] + BLUE * pixel[2]
    
def isCorrupted(fileimage):
    try:
        with Image.open(fileimage) as img:
            img.verify() 
        return False
    except Exception as e:
        print(f'Error opening image: {e}')
        return True
    
def convert_to_grayscale(image_path):
    if not filetype.is_image(image_path):
        print(f'{image_path} is not an image.')
    else :
        if not isCorrupted(image_path) :
            original_image = Image.open(image_path)
        try :
            width, height = original_image.size
            grayscale_image = Image.new("L", (width, height))
            for x in range(width):
                for y in range(height):
                    rgb_pixel = original_image.getpixel((x, y))
                    gray_pixel = gray_scale(rgb_pixel)
                    grayscale_image.putpixel((x, y), int(gray_pixel))
            base_name = os.path.basename(image_path)
            path = os.path.join(OUTPUT_FOLDER, f"grayscale_{base_name}")
            grayscale_image.save(path)
            print(f'Gray Image Saved : {path}')
        except Exception as e :
            print(f'Error while treating image: {e}')
            return



if __name__ == "__main__":

    if USE_FOLDER :
        for file in os.listdir(FOLDER_PATH):
            convert_to_grayscale(os.path.join(FOLDER_PATH, file))
    else : 
        file=input('Type Image path : \n')
        convert_to_grayscale(file)
