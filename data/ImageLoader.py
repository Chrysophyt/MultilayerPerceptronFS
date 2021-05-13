import os, fnmatch
from PIL import Image
import numpy as np
import random
from data.download_extract_data import checkDataset

def convertToGrayscale(imageRGB):
    """return grayscale conversion of RGB image"""
    # https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html
    # Basically  Grayscale = 0.299⋅R + 0.587⋅G + 0.114⋅B
    # We could easily vectorized and just do the dot product of imageRGB with [0.299,0.587,0.114]

    imageGrayscale = np.dot(imageRGB, [0.299,0.587,0.114])

    return imageGrayscale


def getImages(label, n=100):
    """return list of (default 100) images for a given label"""

    # Check Dataset
    checkDataset()

    # Try and get path
    path = "data/flowers/" + label.lower()
    if(not os.path.exists(path)):
        print("No label found")
        return -1
    
    # Get all images address
    allFiles = fnmatch.filter(os.listdir(path), '*.jpg')

    usedFiles = random.sample(allFiles, n) # get 100 samples from allFiles

    # Read the data into numpy array
    imagesRGB = []
    for file in usedFiles:
        img = Image.open(path+'/'+file)
        img = img.resize((320,240), Image.ANTIALIAS)
        imagesRGB.append(np.asarray(img))
    
    imagesRGB = np.asarray(imagesRGB) #(100, 240, 320, 3)

    return imagesRGB

def preprocessImage(images): 
    """return np.array to be loaded into a model,
    flatten dimension (100, 240, 320) -> (100, 76800), and 
    Normalize data value from int [0, 255] -> float [0,1]"""

    x = images.reshape(*images.shape[:1], -1) #(100, 76800)
    x = x/255.0
    return x



