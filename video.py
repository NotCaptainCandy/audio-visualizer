import cv2
import numpy as np
import sys
from tqdm import *

limit = int(float(sys.argv[1]))

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('final.mp4', fourcc, 4, (1000, 1000))

pbar = tqdm(total= limit/4)
counter = 0
index = 0  
while counter < int(limit+1):
    img = cv2.imread(str(counter) + '.png')
    video.write(img)
    counter += 250
    index += 1
    pbar.update(1)

pbar.close()
cv2.destroyAllWindows()
video.release()