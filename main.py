from data.ImageLoader import getImages, convertToGrayscale, preprocessImage

if __name__ == '__main__':
     images = getImages("daisy")
     print(images.shape)

     imagesGray = convertToGrayscale(images)
     print(imagesGray.shape)

     x = preprocessImage(imagesGray)
     print(x.shape)
     