import os
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile


def downloadFlowerData():
    '''Download flower detection dataset from alxmamaev/flowers-recognition.'''
    api = KaggleApi()
    api.authenticate()
    try:
        api.dataset_download_files('alxmamaev/flowers-recognition', path='data/',quiet=False) #do not forget to add kaggle.json into Users/.kaggle/
    except:
        return -1
    return 0

# def getLabels(listLabel):
#     '''Return Image Data from list of labels'''
#     imgData = []
#     for label in listLabel:
#        i = imageLabel.index(label)
#        print("{:04d}".format(i*80+1) + "-" + "{:04d}".format((i+1)*80))

def checkDataset():
    # Check dataset zip file
    if(not os.path.exists('data/flowers-recognition.zip')):
        print("flowers dataset not found, downloading from kaggle")
        if(downloadFlowerData()==-1):
            print("Downloading dataset fail, please check kaggle.json is correct or try again with stable internet connection")
            os.remove('data/flowers-recognition.zip')
            quit()
    
    # Extract Data
    if(not os.path.exists('data/flowers/')):
        print("Extracting flowers-recognition.zip")
        with ZipFile('data/flowers-recognition.zip') as file:
            file.extractall('data/')
        print("Done")

if __name__ == '__main__':
    checkDataset()