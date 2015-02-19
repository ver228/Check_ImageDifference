# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 16:44:30 2015

@author: ajaver
"""
import cv2
import time

import numpy as np
import matplotlib.pylab as plt
from scipy import ndimage
from skimage.measure import regionprops, label
from skimage import morphology
from image_difference import *
import subprocess as sp
import pickle



#fileName = '/Volumes/ajaver$/DinoLite/Videos/Exp5-20150116/A002 - 20150116_140923.wmv';
fileName = '/Volumes/Mrc-pc/GeckoVideo/CaptureTest_90pc_Ch2_16022015_174636.mjpg';
saveName = '/Volumes/ajaver$/GeckoVideo/CaptureTest_90pc_Ch2_16022015_174636.p';


#fileName = '/Volumes/Mrc-pc/GeckoVideo/CaptureTest_85pc_Ch4_13022015_163523.mjpg';
#fileName = '/Volumes/H/GeckoVideo/CaptureTest_85pc_Ch1_13022015_163523.mjpg';
#saveName = '/Volumes/ajaver$/GeckoVideo/CaptureTest_85pc_Ch1_13022015_163523.p';
#fileName = '/Volumes/Mrc-pc/GeckoVideo/CaptureTest_90pc_Ch3_16022015_171848.mjpg';


TOT_PIX = 2048*2048;

command = ['ffmpeg', 
           '-i', fileName,
           '-f', 'image2pipe',
           '-vcodec', 'rawvideo', '-']
pipe = sp.Popen(command, stdout = sp.PIPE, bufsize = TOT_PIX) #use a buffer size as small as possible, makes things faster


tic_first = time.time()
tic = tic_first

max_frames = 100;
tot_frames = 0;



image_prev = np.empty(0);
diffList = []
while 1:#tot_frames < max_frames:
    raw_image = pipe.stdout.read(TOT_PIX)
    
    if len(raw_image) < TOT_PIX:
        break;
    dum = raw_image
    tot_frames += 1;
    
    image = np.fromstring(raw_image, dtype='uint8')
    image = image.reshape(2048,2048)
        
    tot_frames += 1;
    if tot_frames%25 == 1:
        toc = time.time()
        print tot_frames, toc-tic
        tic = toc
    if image_prev.size != 0:
        diffList.append(image_difference(image, image_prev))
    image_prev = image;
    
pipe.stdout.flush()
pickle.dump(diffList, open(saveName, "wb" ))

plt.plot(diffList)
    
#print tot_frames, time.time()- tic
#image = cv2.cvtColor(image, cv2.cv.CV_RGB2GRAY);
#mask = cv2.adaptiveThreshold(image,1,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,61,20)
#label_im, nb_labels = ndimage.label(mask)
#area = ndimage.sum(mask, label_im, range(nb_labels + 1))
#mask_area = area < 1000 & area >20
#
##L = label(mask)
#
#
#
#plt.figure()
#plt.imshow(mask2, cmap = 'gray', interpolation = 'none')
#plt.figure()
#plt.imshow(image, cmap = 'gray', interpolation = 'none')