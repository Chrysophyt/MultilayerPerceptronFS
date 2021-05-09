import os
import requests
import tarfile

from tqdm import tqdm


imageLabel = ['Daffodil','Snowdrop', 'Lily Valley', 'Bluebell', 'Crocus', 'Iris', 'Tigerlily', 'Tulip', 'Fritillary', 'Sunflower', 'Daisy', 'Colts Foot', 'Dandelalion', 'Cowslip', 'Buttercup', 'Windflower', 'Pansy']

def downloadFlowerData():
    '''Download the 17 common flower dataset from https://www.robots.ox.ac.uk/~vgg/data/flowers/17 by Maria-Elena Nilsback and Andrew Zisserman. Data will be downloaded as 17flowers.tgz'''

    print("Starting to download the dataset.")
    imageData = "https://www.robots.ox.ac.uk/~vgg/data/flowers/17/17flowers.tgz"

    response = requests.get(imageData, stream=True)

    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024

    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('17flowers.tgz', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()

    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
        return -1

def getLabels(listLabel):
    '''Return Image Data from list of labels'''
    imgData = []
    for label in listLabel:
        i = imageLabel.index(label)
        print("{:04d}".format(i*80+1) + "-" + "{:04d}".format((i+1)*80))


if __name__ == '__main__':
    datasetfName = '17flowers.tgz' 

    #Check if dataset available
    if(not os.path.isfile(datasetfName)):
        downloadFlowerData()
    else:
        print('Dataset already exists.')

    #Check if path available
    if(not os.path.isdir('jpg')):
        print("Extracting Dataset.")
        tar = tarfile.open(datasetfName, "r:gz")
        tar.extractall()
        tar.close()
        print("Done")
    else:
        print('Directory already exists.')

    getLabels(['Daffodil', 'Pansy'])