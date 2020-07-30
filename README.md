# Photomosaic maker
Given an original image and another set of images (to make the final image out of), this code can generate a photomosaic in ~ 1 min!

See an example of photomosaic Morgan Freeman [here!](final_pic_morgan.png)

### Prerequisites
- Python 2.6 or greater
- The pip package management tool
- A Google account
- A Spotify account

### Local Setups
Install all dependencies: 
```
pip install -r requirements.txt
```

### Start-up Instructions (resizing pictures)
1. Download an image set you want to use to make up your picture. (I used kaggle to find image sets) 
2. Change the path on the [resize_small_pics.py](resize_small_pics.py) file to where ever your folder is stored. 
2. Run the [resize_small_pics.py](resize_small_pics.py) file to resize photos ready to use in the main script. 

### Running Main File (creating the photomosaic)
There are several things you need to change in the [photomosaic_maker.py](photomosaic_maker.py) file to make sure it works on your computer.

line 9: The dom_factor_dict is there to make sure your final image looks as close to the original image as possible. I've got it in dictionary form simply because I was using a few image sets and each had a differrent best dominant factor. The dominant factor needs to be between 0 and 1. It works by only using images in your dataset where the dominant colour of the picture is greater than that of the dominant factor. For example, a dominant factor of 0.7 would ensure that the images used to make up the final picture all have over 70% of the picture being made up of just one dominant colour. This factor can be changed up or down depending on the image set used and the original picture used. 

line 13: Read line in file
line 14: Read line in file

line 21: pixel_factor - May or may not need to be changed. I've optimised to the size I like the pixels to look in the final image, but this can be increased to increase pixel size, or decreased to decrease pixel size.

line 36: Read line in file
line 72: Read line in file

After these changes have been made the file can be run! The image can take 1-2 mins to run depending on the size of the original photo. 
