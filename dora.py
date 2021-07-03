#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFilter
import random
import os
import glob

path = ""
img_path = ""
home_fl = ""

ff = [f"{path}/*.png", f"{path}/*.PNG", f"{path}/*.JPG", f"{path}/*.jpg", f"{path}/*.jpeg", f"{path}/*.JPEG"]
posfil = []

for i in ff:
    for x in glob.glob(i):
        posfil.append(x)

dora = Image.open(img_path)

for i in posfil:
    v_img = Image.open(i)

    cor_w = int(v_img.size[0]/4)
    cor_h = int(cor_w + (cor_w * 20)/100)

    temp_dora = dora.resize((cor_w, cor_h))
    temp_dora = temp_dora.convert("RGBA")

    mask_im = Image.new("L", (cor_w, cor_h), 0)
    draw = ImageDraw.Draw(mask_im)
    
    ten_p_w = (cor_w * 10)/100
    ten_p_h = (cor_h * 10)/100
    
    draw.ellipse((ten_p_w, ten_p_h, cor_w - ten_p_w, cor_h - ten_p_h), fill=255)
    mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))

    v_img.paste(temp_dora, (random.randrange(0, v_img.size[0]), random.randrange(0, v_img.size[1])), mask_im_blur)
    v_img.save(i, quality=95)
    print(f"Infection on {i} was successfull")
