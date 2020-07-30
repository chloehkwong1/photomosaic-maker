from PIL import Image
import os.path
from pathlib import Path
import extcolors
from natsort import natsorted

'''Change these variables if necessary!'''
#rough best percentages for each image dataset(but further experimentation can be beneficial)
dom_factor_dict = {
    "FOLDER NAME CONTAINING YOUR IMAGE SET" : 0.7,
    "CAN STORE MULTIPLE DATASETS HERE SO YOU CAN KEEP TRACK OF THE DOMINANT FACTOR PERCENTAGE" : 0.5
}
im_name = "YOUR ORIGINAL PIC.jpeg"
image_dataset = "FOLDER NAME CONTAINING YOUR IMAGE SET"

start_im = Image.open(im_name)

def pixelator():
    #increase denominator to increase pixel size
    #good initial starting pixel_factor = start_im.size[0]/165
    pixel_factor = max(start_im.size[0],start_im.size[1])/165
    im_final = start_im.resize((int(start_im.size[0]/pixel_factor), int(start_im.size[1]/pixel_factor)))
    return im_final

def rgb_pixel(im_final):
    rgb_im_avg = []
    for y in range(im_final.size[1]):
        y_im_avg = []
        for x in range(im_final.size[0]):
            y_im_avg.append(im_final.getpixel((x,y)))
        rgb_im_avg.append(y_im_avg)
    return rgb_im_avg

def rgb_avg_pics():
    #change path ending depending on which small pictures are wanted
    new_path = Path("PATH TO FOLDER WHERE YOUR IMAGE SET IS", 'resized_pics')
    try:
        new_dir = os.listdir(new_path)
        colour_dict = {}
        for item in new_dir:
            fullpath = os.path.join(new_path,item)
            if os.path.isfile(fullpath):
                img = Image.open(fullpath)        
                colours, pixel_count = extcolors.extract_from_image(img)
                percentage_dom_colour = colours[0][1]/pixel_count
                if percentage_dom_colour > dom_factor_dict[image_dataset]:
                    colour_dict[item] = colours[0][0]
        return colour_dict, new_path
    except FileExistsError:
        print("Error: that folder doesn't exist.")
        
def match_pics_and_pixels(rgb_im_avg, colour_dict):
    match_pixel_img = []
    for row in rgb_im_avg:
        int_match = []
        for item in row:
            r1, g1, b1 = item
            min_distance = float("inf")
            best_match = ""
            for key, value in colour_dict.items():
                r2, g2, b2 = value
                #try using CIELAB color space!!
                distance = ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)**0.5
                if distance < min_distance:
                    best_match = key
                    min_distance = distance
            int_match.append(best_match)
        match_pixel_img.append(int_match)
    return match_pixel_img
        
def concat_rows(match_pixel_img, new_path):
        path = "PATH TO WHERE YOU WANT TO STORE YOUR NEW PHOTOMOSAIC FOLDER"
        counter_1 = 1
        while True:
            try:
                new_path_concat = Path(path, im_name + "_with_" + image_dataset + "_" + str(dom_factor_dict[image_dataset]) + "_" + str("%.2d" % counter_1))
                new_path_concat.mkdir(parents=True, exist_ok=False)
            except FileExistsError:
                counter_1 += 1
            else:
                break
            
        counter_2 = 0
        for row in match_pixel_img:
            im1_path = os.path.join(new_path,row.pop(0))
            im1 = Image.open(im1_path)
            counter_2 += 1
            for im2 in row:
                fullpath = os.path.join(new_path,im2)
                if os.path.isfile(fullpath):
                    im2 = Image.open(fullpath)
                    x = Image.new('RGB', (im1.width + im2.width, min(im1.height, im2.height)))
                    x.paste(im1, (0, 0))
                    x.paste(im2, (im1.width, 0))
                    im1 = x
                    
            final_path = os.path.join(new_path_concat, "concat_rows_" + str("%.2d" % counter_2) + ".png") 
            x.save(final_path, "PNG", quality=100)
        return new_path_concat

def concat_pic(new_path_concat):
    concat_dir = natsorted(os.listdir(new_path_concat))
    im1_path = os.path.join(new_path_concat,concat_dir.pop(0))
    im1 = Image.open(im1_path)
    for image in concat_dir:
        fullpath = os.path.join(new_path_concat,image)
        if os.path.isfile(fullpath):
            im2 = Image.open(fullpath)
            x = Image.new('RGB', (im1.width, im1.height + im2.height))
            x.paste(im1, (0, 0))
            x.paste(im2, (0, im1.height))
            im1 = x
    final_path = os.path.join(new_path_concat, "final_pic.png") 
    x.save(final_path, "PNG", quality=100)
    return x.show()
        
if __name__ == '__main__':
    im_final = pixelator()
    rgb_im_avg = rgb_pixel(im_final)
    colour_dict, new_path = rgb_avg_pics()
    match_pixel_img = match_pics_and_pixels(rgb_im_avg, colour_dict)
    new_path_concat = concat_rows(match_pixel_img, new_path)
    concat_pic(new_path_concat)
