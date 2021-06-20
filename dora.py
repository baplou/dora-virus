#!/usr/bin/env python3
import PIL
import os
import glob

path = ""

def get_files():
    posfil = glob.glob(f"{path}/*.png")

    for i in glob.glob(f"{path}/*.jpg"):
        posfil.append(i)

    for i in glob.glob(f"{path}/*.PNG"):
        posfil.append(i)

    for i in glob.glob(f"{path}/*.JPG"):
        posfil.append(i)

    for i in posfil:
        print(i)

if __name__ == "__main__":
    get_files()
