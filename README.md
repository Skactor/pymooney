# pymooney

## Overview
This repository helds the python scripts to generate twotone, Mooney images. The main code is crmooney.py.

You can

(i) you can give a directory with images

(ii) you can give one image path

The easiest way to use these scripts is to check the main-function in crmooney.py and write a wrapper funciton based on that.



## Requirements

*   scipy

*   numpy

*   skimage

You can download them from https://www.lfd.uci.edu/~gohlke/pythonlibs/

## Modifies

1.  Drop the flickr.com support because of the obsolete of flickrapi
2.  Add support for newest matplotlib

## Citation
========

Please cite our Neuroimage paper if you use this package to create Mooney images.

[Fatma Imamoglu, Thorsten Kahnt, Christof Koch, John-Dylan Haynes, Changes in functional connectivity support conscious object recognition, NeuroImage, Volume 63, Issue 4, December 2012, Pages 1909–1917](http://www.sciencedirect.com/science/article/pii/S1053811912007860)
