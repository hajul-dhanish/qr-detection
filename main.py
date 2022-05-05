import cv2 as cv 
import numpy as np
im = cv.imread("qrcode.png")
det = cv.QRCodeDetector()
rv, pts = det.detectMulti(np.hstack([im, im])) 
print("multiple:", rv) # True