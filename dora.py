#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFilter
import random
import os
import glob

path = ""
img_path = ""
home_fl = ""

posfil = glob.glob(f"{path}/*.png")

for i in glob.glob(f"{path}/*.jpg"):
    posfil.append(i)
for i in glob.glob(f"{path}/*.PNG"):
    posfil.append(i)
for i in glob.glob(f"{path}/*.JPG"):
    posfil.append(i)

dora = Image.open(img_path)
for i in posfil:
    v_img = Image.open(i)
    cor_w = int(v_img.size[0]/4)
    cor_h = int((20 * cor_w)/100)

    temp_dora = dora.resize((cor_w, cor_h))
    temp_dora = temp_dora.convert("RGBA")

    # check img format thingy
    mask_im = Image.new("RGBA", (cor_w, cor_h), 0)
    draw = ImageDraw.Draw(mask_im)
    # fix me
    # weirdo math
    draw.ellipse(((cor_w/4)/2, (cor_h/4)/2, cor_w - (cor_w/4), cor_h - (cor_h/4)), 255, 0)
    mask_im = mask_im.filter(ImageFilter.GaussianBlur(10))

    v_img.paste(temp_dora, (random.randrange(0, v_img.size[0]), random.randrange(0, v_img.size[1])), mask_im_blur)
    v_img.save(i, quality=95)
