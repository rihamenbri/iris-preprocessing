import numpy as np
import matplotlib.pyplot as plt
import cv2

from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny


def mask (image, Fcint, Fcext, cxe, cye, cxi, cyi):
    nl= image.shape[0]
    nc=  image.shape[1]
    xe = np.arange(-cxe[0],nc-cxe[0],1)
    ye = np.arange(-cye[0],nl-cye[0],1)
    xxe, yye = np.meshgrid(xe, ye, sparse=True)
    ze = np.sqrt(xxe*xxe + yye*yye)
    xi = np.arange(-cxi[0],nc-cxi[0],1)
    yi = np.arange(-cyi[0],nl-cyi[0],1)
    xxi, yyi = np.meshgrid(xi, yi, sparse=True)
    zi = np.sqrt(xxi*xxi + yyi*yyi)
    
    return (ze<Fcext)*(Fcint<zi)

def seg (image) :   
# Thresholding and edge detection
    ret1,th1 = cv2.threshold(image,35,255,cv2.THRESH_BINARY)
    edgesint= canny(th1, sigma=3, low_threshold=150, high_threshold=255)

    ret2,th2 = cv2.threshold(image,100,255,cv2.THRESH_BINARY)
    edgesext = canny(th2, sigma=3, low_threshold=150, high_threshold=255)

# calculate hough radius
    hough_radiii = np.arange(10, 2000)
    hough_resi = hough_circle(edgesint, hough_radiii)

    hough_radiie = np.arange(50, 2000)
    hough_rese = hough_circle(edgesext, hough_radiie)

# Select the most prominent 2 circles
    accumsi, cxi, cyi, radiii = hough_circle_peaks(hough_resi, hough_radiii,total_num_peaks=1)
    accumse, cxe, cye, radiie = hough_circle_peaks(hough_rese, hough_radiie,total_num_peaks=1)
    
    if ( len(cxi)!= 0 ) and (len(cxe)!= 0) and ( len(cyi)!= 0 ) and (len(cye)!= 0):
        Seg = (image) * mask (image, radiii, radiie, cxe, cye, cxi, cyi)
        return Seg, cxi[0],cyi[0], radiii[0], radiie[0]
    
    else : return []
