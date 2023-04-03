import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def reflect(gray):
    # reflections' localizing and enhancement  
    ret1,th1 = cv.threshold(gray,200,255,cv.THRESH_BINARY)
    refpart = gray*(th1//255)
    refpart  = refpart.astype('uint8')
    ref_HE= cv.equalizeHist(refpart)
    
    # image totally enhaced 
    img_enh_f = gray - th1 + ref_HE
    
    return img_enh_f 
