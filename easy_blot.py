import os, shutil
from scipy import misc
import Image
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

blots = []
immuno = []
# Then we recursively traverse through each folder
# and match each file against our list of files to find.
for root, dirs, files in os.walk('/Volumes/Daten/Dropbox/Bachelor Results/'):
    for _file in files:
        if '.tif' in _file and 'WB' in root:
            blots.append(root+ '/' +_file)


for blot in blots:
    im = misc.imread(blot)
    lx, ly, lz = im.shape
    plt.figure(figsize=(6*2,4*2))
    imgplot = plt.imshow(im[0:lx, 0:ly], cmap=plt.cm.gray)
    plt.grid(True)
    plt.xticks(range(75, 600, 50))
    plt.show()
    print 'image dimensions: %d, %d' % (lx, ly)
    crop = raw_input('Set Cropping dimension, separate by commas (x1, x2, y1, y2):')
    x1, y1 = crop.split(', ')
    x2 = int(x1) + 400
    y2 = int(y1) + 150
    plt.figure(figsize=(6*1.5,4*1.5))
    imgplot = plt.imshow(im[int(y1):int(y2), int(x1):int(x2)], cmap=plt.cm.gray)
    plt.grid(True)
    plt.show()
    print blot.split('/')[-1]
    annotation = raw_input('Annotate the blot? ')
    if annotation=='y':
        question = raw_input('Set X1, X2, and Y:')
        bands = raw_input('What is on the lanes: ')
        band1, band2 = bands.split(', ')
        X1, X2, Y = question.split(', ')
        X3 = int(X2)+10
        X4 = X3+(int(X2)-int(X1))
        plt.figure(figsize=(6*1.5,4*1.5))
        imgplot = plt.imshow(im[int(y1):int(y2), int(x1):int(x2)], cmap=plt.cm.gray)
        plt.grid(True)
        plt.autoscale(enable=False, axis='both')
        plt.plot([X1, X2], [Y, Y], 'k-', lw=2)
        plt.plot([X3, X4], [Y, Y], 'k-', lw=2)
        plt.text(((int(X2)-int(X1))/2), int(Y)+10, band1, style='italic', bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})
        plt.text(np.median(range(X3, X4)), int(Y)+10, band2, style='italic', bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})
        plt.show()
    user = raw_input('Want to save (y or n)? ')
    if user == 'y':
        savepath= '/Volumes/Daten/Dropbox/Bachelor Results/' + blot.split('/')[-1]
        plt.imshow(im[int(y1):int(y2), int(x1):int(x2)], cmap=plt.cm.gray)
        plt.savefig(savepath)
    elif user=='n':
        break
