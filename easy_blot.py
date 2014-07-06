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

def getBlotDimension(blot):
    '''
    Takes a blot as input and returns X- and Y-directions
    '''
    lx, ly, lz = blot.shape
    return lx, ly

def getBlotName(blot):
    return blot.split('/')[-1]

def getBlotDate(blot):
    filename = getBlotName(blot)
    return filename[0:10]


def showBlot(blot):
    '''
    Takes a blot as input.

    Returns a enlarged image of the blot.
    '''
    #xmax, ymax = getBlotDimension(blot)
    plt.figure(figsize=(6*2,4*2))
    imgplot = plt.imshow(blot, cmap=plt.cm.gray)
    plt.grid(True)
    plt.xticks(range(0, 600, 25), rotation=25)
    plt.yticks(range(0, 400, 25))
    plt.show()

def cropBlot(blot, X1, Y1):
    '''
    Takes a blot and X1, Y1 coordinates as input. Based on the coordinates,
    cropBlot will set X2 and Y2 automatically. The user may set the value that
    is added to X1 and Y2 in the following lines

    Returns the blot as a resized matrix.
    '''
    X2 = int(X1) + 400
    Y2 = int(Y1) + 150

    croppedBlot = blot[int(Y1):int(Y2), int(X1):int(X2)]

    return croppedBlot

def setBar(blot, X1, X2, Y):

    X3 = int(X2)+10
    X4 = X3+(int(X2)-int(X1))
    imgplot = plt.imshow(blot, cmap=plt.cm.gray)
    plt.autoscale(enable=False, axis='both')
    plt.plot([X1, X2], [Y, Y], 'k-', lw=2)
    plt.plot([X3, X4], [Y, Y], 'k-', lw=2)



def isOk():
    '''
    Simple function that return True if the user is satisfied with his work.
    '''
    ok = raw_input('OK? ')
    if ok == 'y':
        return True
    else:
        return False


for blot in blots:
    im = misc.imread(blot)
    showBlot(im)
    getBlotDimension(im)

    print getBlotName(blot)

    cropProcedure = False
    annotateProcedure = False

    while cropProcedure != True:
        crop = raw_input('Set Cropping dimension, separate by commas (x1, y1):')
        X1, Y1 = crop.split(', ')
        croppedBlot = cropBlot(im, X1, Y1)
        showBlot(croppedBlot)
        cropProcedure = isOk()

    #print blot.split('/')[-1]
    while annotateProcedure != True:
        print getBlotName(blot)
        annotation = raw_input('Annotate the blot? ')
        if annotation=='y':
            question = raw_input('Set X1, X2, and Y:')
            bands = raw_input('What is on the lanes? Antibody?: ')

            band1, band2, ak = bands.split(', ')
            X1, X2, Y = question.split(', ')
            X3 = int(X2)+10
            X4 = X3+(int(X2)-int(X1))

            imgplot = plt.imshow(croppedBlot, cmap=plt.cm.gray)

            plt.grid(True)
            plt.autoscale(enable=False, axis='both')

            # Set the bars

            plt.plot([X1, X2], [Y, Y], 'k-', lw=2)
            plt.plot([X3, X4], [Y, Y], 'k-', lw=2)

            # Show text

            plt.text(((int(X2)-int(X1))/2), int(Y)+20, band1, style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})
            plt.text(((int(X4)-int(X3))/2)*3, int(Y)+20, band2, style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})

            plt.title(getBlotDate(blot) + ' ' + str(ak))

            plt.show()

            annotateProcedure = isOk()

    print getBlotName(blot)
    user = raw_input('Want to save (y or n)? ')

    if user == 'y':
        savepath= '/Volumes/Daten/Dropbox/Bachelor Results/' + blot.split('/')[-1]

        imgplot = plt.imshow(croppedBlot, cmap=plt.cm.gray)

        #plt.grid(True)
        plt.autoscale(enable=False, axis='both')

        # Set the bars

        plt.plot([X1, X2], [Y, Y], 'k-', lw=2)
        plt.plot([X3, X4], [Y, Y], 'k-', lw=2)

        # Show text

        plt.text(((int(X2)-int(X1))/2), int(Y)+20, band1, style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})
        plt.text(((int(X4)-int(X3))/2)*3, int(Y)+20, band2, style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})

        # Get rid of the x and y-axis

        plt.axis('off')
        #plt.tick_params(which='both', bottom='off', top='off', labelbottom='off')
        #plt.tick_params(axis='y', which='both', bottom='off', top='off', labelbottom='off')

        plt.title(getBlotDate(blot) + ' ' + str(ak))

        plt.savefig(savepath)

    elif user=='n':
        break
