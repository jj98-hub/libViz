from genericpath import isdir
import pandas as pd
import numpy as np
import cv2 
import os


class UI:
    def __init__(self,size = (6,6)):
        self.header = []
        self.size = size
        self.dataSize = size[0]*size[1]
        for i in range(self.dataSize):
            self.header.append(str(i+1))
    
    def readCSV(self,path):
        self.df = pd.read_csv(path)
        try:
            self.numpyData = self.df[self.header]
            self.numpyData = self.numpyData.to_numpy(dtype='uint8')
            return self.numpyData
        except:
            print('Error! The input dimension of "UI(size = )" is bigger than data from csv file')
    

    
    def userInterfaceCreate(self,name = 'Data Visualization'):
        cv2.namedWindow(name)
    
    def updateOnPress (self, dataNumpy,save = False):
        if dataNumpy is not None:
            for i in range (len(dataNumpy)):
                self.img = dataNumpy[i].reshape(self.size)
                self.img = cv2.resize(self.img,(600,600))
                self.img = cv2.applyColorMap(self.img,cv2.COLORMAP_JET)
                cv2.imshow('Data Visualization',self.img)
                cv2.imshow('Data Visualization',self.img)
                if save == True:
                    self.saveImages(self.img,"imageLogging",i)
                key = cv2.waitKey(0)
                if key == 27:
                    break
            cv2.destroyAllWindows()  

    def saveImages(self,img,folderPath,filename):
        if img is not None:
            dirPath = str(folderPath)
            if not os.path.exists(dirPath):
                os.mkdir(dirPath)
            imgPath = str(folderPath)+'/'+str(filename)+'.jpg'
            cv2.imwrite(imgPath,img)
    
    def updateUserInterfaceData(self, dataNumpy,sleep=100,save = False): #the sleep is in miliseconds
        if dataNumpy is not None:
            for i in range (len(dataNumpy)):
                self.img = dataNumpy[i].reshape((self.size))
                self.img = cv2.resize(self.img,(600,600))
                self.img = cv2.applyColorMap(self.img,cv2.COLORMAP_JET)
                cv2.imshow('Data Visualization',self.img)
                if save == True:
                    self.saveImages(self.img,"imageLogging",i)
                key = cv2.waitKey(sleep)
                if key == 27:
                    break
            cv2.destroyAllWindows()




if __name__ == '__main__':
    myUI = UI(size=(6,6))
    data = myUI.readCSV('example.csv')
    myUI.userInterfaceCreate()
    myUI.updateUserInterfaceData(data,100,save=True)
    # myUI.updateOnPress(data)
