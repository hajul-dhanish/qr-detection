#  It Will check for multiple qr Codenin a single and return true if its detected

import cv2 as cv 
import numpy as np
im = cv.imread("assets/single.jpeg")
det = cv.QRCodeDetector()
rv, pts = det.detectMulti(np.hstack([im, im])) 
print("multiple:", rv) # True