from natsort import natsorted
from PIL import Image
import os
import argparse

def rescale_images(dataset, directory, size):
    for img in natsorted(os.listdir(dataset)):
        im = Image.open(dataset+img)
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(directory+img)
        print("Initial size: {}".format(im.size))
        print("{}".format(im_resized.format))
        print("Resized size: {}".format(im_resized.size))
        print("image mode: {}".format(im_resized.mode))
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-ds', '--dataset', type=str, required=True, help='Dataset containing the images')
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory saving the images')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Image size')
    args = parser.parse_args()
    rescale_images(args.dataset, args.directory, args.size)
