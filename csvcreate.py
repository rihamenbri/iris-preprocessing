import csv
import os 
import cv2 as cv
from final import prepro


labels=[]
label_id={}  # labels dictionnary

with open('dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for root, dir, imgs in os.walk('CASIA'):
        for img in imgs :
            if img.endswith('bmp') :
                path= os.path.join(root, img)
                label = os.path.basename(os.path.dirname(path)) 
                 
                if not (label in labels) :
                    labels.append(label)
                    label_id [label] = len(labels)-1  # encoding of labels starting from 0
                   
                img = prepro(path)
                
                if img != 0 :
                    writer.writerow([img, label_id[label]])
                
            