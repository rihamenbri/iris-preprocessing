import numpy as np

def norm (image, cxi,cyi, radiii, radiie):
    
    theta = np.arange(0, 360, 1) #theta
    rad = np.arange(0, (radiie-radiii), 1) #radius
    
    normal = np.empty(shape = [rad.size, theta.size, 3])
    
    for t in theta:
        for r in rad:
            polarX = int(((r+radiii) * np.cos(t*3.14/180)) + cxi)
            polarY = int(((r+radiii) * np.sin(t*3.14/180)) + cyi)
            normal[int(r)][int(t) - 1] = image[polarY][polarX]
            normal = normal.astype('uint8')
    return normal

