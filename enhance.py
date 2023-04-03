import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def gammaCorrection(img, gamma):
    table = np.array([((i / 255) ** (gamma)) * 255 for i in range(256)])
    return cv.LUT(img, table)

def gamma (grayimg):     
    hist, bins = np.histogram(grayimg , bins= np.arange(0,256)) 
    if(len(hist)!=len(bins)):
        hist = np.append(hist, 0 )
    index = np.where(hist == max(hist))[0][0]
    if (index>160):
        return 0.9
    else :
        if (index < 60): 
            return 1.1
        else : return 1   
    
def enh(gray) :
    # enhacement of the image
    hist = cv.equalizeHist(gray)
    med= cv.medianBlur(hist,3)
    GIC = gammaCorrection(med,gamma(gray))
    filterSize =(3, 3)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, filterSize)  
    img1 = cv.morphologyEx(GIC, cv.MORPH_TOPHAT,kernel)
    img2 = gray - cv.morphologyEx(img1, cv.MORPH_BLACKHAT,kernel)
    return img2


    



