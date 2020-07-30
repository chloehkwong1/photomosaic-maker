from PIL import Image
import os.path
from pathlib import Path


#resizes all pictures in a directory
def resize():
    '''
    change path as necessary to resize different set of pictures
    '''
    path = "C:/Users/PATH TO YOUR FOLDER CONTAINING IMAGE SET
    dirs = os.listdir(path)
    new_path = Path(path, 'resized_pics')
    new_path.mkdir(parents=True, exist_ok=True)
    for item in dirs:
        fullpath = os.path.join(path,item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.split(fullpath)
            final_path = os.path.join(new_path, "resized_" + e)
            imResize = im.resize((50,50))  
            imResize.save(final_path, quality=100)

if __name__ == '__main__':
    resize()

    
