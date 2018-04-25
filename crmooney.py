#!/usr/bin/env python

import os

import utils_image


def crmooney_frompath(filename, mooneypath='', resize=False, smooth_sigma=6, image_size=(400, 400), threshold_method='global_otsu'):
    """ Given a path create and save Mooney images in the directory specified with

    Input:
        filename: Can be a directory (in which case all the .JPG files will be converted to Mooney) or the path of the jpg file.
        mooneypath: Path to save the final Mooney image.

    Returns:
        imgs_mooney: A dictionary of Mooney images along with the threshold value, its original path and original image name.
    """

    if mooneypath == '':
        if not os.path.dirname(filename) == '':
            mooneypath = os.path.dirname(filename)
        else:
            mooneypath = os.getcwd()

    # Load image
    imgs = utils_image.load_imgs(filename)

    imgs_mooney = []
    for imgname, img in imgs.items():

        # Convert to gray scale image
        if len(img.shape) > 2:
            img = utils_image.rgb2gray(img)
            fname = os.path.join(mooneypath, imgname.split('.')[0] + '_g.' + imgname.split('.')[1])
            utils_image.save_img(img, fname)

        # Resize image
        if resize:
            img = utils_image.resize_img(img, image_size)
            fname = os.path.join(mooneypath, imgname.split('.')[0] + '_gr.' + imgname.split('.')[1])
            utils_image.save_img(img, fname)

        # Smooth image
        img = utils_image.gauss_filter(img, sigma=smooth_sigma)
        fname = os.path.join(mooneypath, imgname.split('.')[0] + '_s.' + imgname.split('.')[1])
        utils_image.save_img(img, fname)

        # Create Mooney image
        img, threshold = utils_image.threshold_img(img, method=threshold_method)
        fname = os.path.join(mooneypath, imgname.split('.')[0] + '_m.' + imgname.split('.')[1])
        utils_image.save_img(img, fname)

    print '{0} Mooney images are in {1} and in the return variable'.format(len(imgs_mooney), mooneypath)


if __name__ == '__main__':
    # Create images from a given path
    imagepath = os.path.join(os.getcwd(), 'images')

    mooneypath = os.path.join(imagepath, 'mooney')
    crmooney_frompath(imagepath, mooneypath=mooneypath, resize=True, smooth_sigma=1)
