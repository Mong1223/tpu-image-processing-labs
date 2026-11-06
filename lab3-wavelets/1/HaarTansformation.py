from PIL import Image, ImageFont, ImageDraw
import numpy as np
from math import sqrt


class HaarTransformation:

    def __init__(self, imageName):
        try:
            self.image = Image.open(imageName)
        except Exception as error:
            print(f"No image with name: : {imageName}")
        self.imageSize = list(self.image.size)
        # load greyscale image
        self.image = self.image.convert('L')
        # check the size of image
        if self.imageSize[0] % 2 != 0:
            self.imageSize[0] -= 1
        if self.imageSize[1] % 2 != 0:
            self.imageSize[1] -= 1

        # cut the image
        self.image = self.image.crop((0, 0, self.imageSize[0], self.imageSize[1]))
        self.imageBuff = np.array(self.image)
        self.imageBuff = self.imageBuff.astype('float')
        self.power = 0

    def printImage(self):
        self.image.show()

    def __del__(self):
        self.image.close()

    # def getHaarMatrix(self, n, m):
    #
    #     matrix = np.zeros((n, n))
    #     iter = 0
    #     for i in range(n // 2):
    #         matrix[i, iter] = 1
    #         matrix[i, iter + 1] = 1
    #         matrix[i + n // 2, iter] = 1
    #         matrix[i + n // 2, iter + 1] = -1
    #         iter += 2
    #
    #     return matrix

    def getDobeshiMatrix(self, n, m):
        c1 = (1 + sqrt(3)) / (4 * sqrt(2))
        c2 = (3 + sqrt(3)) / (4 * sqrt(2))
        c3 = (3 - sqrt(3)) / (4 * sqrt(2))
        c4 = (1 - sqrt(3)) / (4 * sqrt(2))

        matrix = np.zeros((n, n))
        iter1 = 0
        iter2 = iter1 + 2

        for i in range(n // 2):
            matrix[i, iter1] = c1
            matrix[i, iter1 + 1] = c2
            matrix[i, iter2] = c3
            matrix[i, iter2 + 1] = c4
            matrix[i + n // 2, iter1] = c4
            matrix[i + n // 2, iter1 + 1] = -c3
            matrix[i + n // 2, iter2] = c2
            matrix[i + n // 2, iter2 + 1] = -c1

            if iter1 < n - 2:
                iter1 += 2
            else:
                iter1 = 0
            if iter2 < n - 2:
                iter2 += 2
            else:
                iter2 = 0

        return matrix

    def directDobeshi(self):
        _shape = (self.imageBuff.shape[0] // 2 ** self.power, self.imageBuff.shape[1] // 2 ** self.power)
        arrayImage = self.imageBuff[:_shape[0], :_shape[1]].copy()
        arrayImage = arrayImage.transpose()
        dobeshiMatrix = self.getDobeshiMatrix(arrayImage.shape[0], arrayImage.shape[1])
        newImage = np.matmul(dobeshiMatrix, arrayImage)
        newImage = newImage.transpose()
        arrayImage = newImage.copy()
        dobeshiMatrix = self.getDobeshiMatrix(arrayImage.shape[0], arrayImage.shape[1])
        newImage = np.matmul(dobeshiMatrix, arrayImage)
        self.imageBuff[:_shape[0], :_shape[1]] = newImage.copy()
        self.power += 1

    def reverseDobeshi(self):
        self.power -= 1
        _shape = (self.imageBuff.shape[0] // 2 ** self.power, self.imageBuff.shape[1] // 2 ** self.power)
        arrayImage = self.imageBuff[:_shape[0], :_shape[1]].copy()
        dobeshiMatrix = self.getDobeshiMatrix(arrayImage.shape[0], arrayImage.shape[1]).transpose()
        newImage = np.matmul(dobeshiMatrix, arrayImage)
        newImage = newImage.transpose()
        arrayImage = newImage.copy()
        dobeshiMatrix = self.getDobeshiMatrix(arrayImage.shape[0], arrayImage.shape[1]).transpose()
        newImage = np.matmul(dobeshiMatrix, arrayImage)
        newImage = newImage.transpose()
        self.imageBuff[:_shape[0], :_shape[1]] = newImage.copy()

    def directHaar(self):
        arrayImage = self.imageBuff.copy()
        newArray = arrayImage.copy()
        arrayImage = arrayImage.transpose()
        newArray = newArray.transpose()
        iter = 0
        shape = (arrayImage.shape[0] // 2 ** self.power, arrayImage.shape[1] // 2 ** self.power)
        for i in range(shape[0] // 2):
            newArray[i][:shape[1]] = (arrayImage[iter][:shape[1]] + arrayImage[iter + 1][:shape[1]]) / 2
            newArray[i + shape[0] // 2][:shape[1]] = (arrayImage[iter][:shape[1]] - arrayImage[iter + 1][:shape[1]]) / 2
            iter += 2
        arrayImage = newArray.copy().transpose()
        newArray = newArray.transpose()
        iter = 0
        shape = (arrayImage.shape[0] // 2 ** self.power, arrayImage.shape[1] // 2 ** self.power)
        for i in range(shape[0] // 2):
            newArray[i][:shape[1]] = (arrayImage[iter][:shape[1]] + arrayImage[iter + 1][:shape[1]]) / 2
            newArray[i + shape[0] // 2][:shape[1]] = (arrayImage[iter][:shape[1]] - arrayImage[iter + 1][:shape[1]]) / 2
            iter += 2
        newArray[:shape[0], :shape[1]] /= sqrt(2)
        self.imageBuff = newArray.copy()
        self.power += 1

    def reverseHaar(self):
        arrayImage = self.imageBuff.copy()
        self.power -= 1
        shape = (arrayImage.shape[0] // 2 ** self.power, arrayImage.shape[1] // 2 ** self.power)
        arrayImage[:shape[0], :shape[1]] *= sqrt(2)
        newArray = arrayImage.copy()
        iter = 0
        for i in range(0, shape[0], 2):
            newArray[i][:shape[1]] = (arrayImage[iter][:shape[1]] + arrayImage[iter + shape[0] // 2][:shape[1]])
            newArray[i + 1][:shape[1]] = (arrayImage[iter][:shape[1]] - arrayImage[iter + shape[0] // 2][:shape[1]])
            iter += 1
        arrayImage = newArray.copy().transpose()
        newArray = newArray.transpose()
        iter = 0
        shape = (arrayImage.shape[0] // 2 ** self.power, arrayImage.shape[1] // 2 ** self.power)
        for i in range(0, shape[0], 2):
            newArray[i][:shape[1]] = (arrayImage[iter][:shape[1]] + arrayImage[iter + shape[0] // 2][:shape[1]])
            newArray[i + 1][:shape[1]] = (arrayImage[iter][:shape[1]] - arrayImage[iter + shape[0] // 2][:shape[1]])
            iter += 1
        newArray = newArray.transpose()
        self.imageBuff = newArray.copy()

    def printImageFromBuf(self, text):
        if self.imageBuff is not None:
            buff = self.imageBuff.copy()
            buff = Image.fromarray(np.uint8(buff))
            # buff.show()
            width, height = buff.size
            bi = Image.new('RGBA', (width + 10, height + np.uint(height / 5)), 'white')
            bi.paste(buff, (5, 5, (width + 5), (height + 5)))
            font = ImageFont.truetype("arial.ttf", 45)
            w, h = font.getsize(text)

            draw = ImageDraw.Draw(bi)
            draw.text(((width - w) / 2, (height + ((height / 5) - h) / 2)), text, font=font, fill="black")
            bi.show()
        else:
            raise Exception("Image wasn't created")
