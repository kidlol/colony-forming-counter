import os
import cv2 as cv
import numpy as np
import random as rng
from flask import jsonify 
rng.seed(12345)

def image_make(file_name):
    folder='uploads'
    # threshold = file_name
    src = cv.imread(os.path.join(folder,file_name))

    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    src_gray = cv.blur(src_gray, (3,3))

    # src_thres = cv.threshold(src_gray, 6, 255, cv.THRESH_BINARY)[1]  # ensure binary

    # Detect edges using Canny
    canny_output = cv.Canny(src_gray, 6, 6 * 2)
    # Find contours
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Draw contours
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        # color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.drawContours(drawing, contours, i, (0,255,0), 1, cv.LINE_8, hierarchy, 0)
    # Show Image
    cv.imwrite(os.path.join(folder,file_name),drawing)
    print ("Number of Objects is " , int(len(contours)/2))
    # Parsing ke bentuk JSON response
    hasil = int(len(contours)/2)
    #hitung hasil Koloni
    message = {
        'status': 'Success',
        'data': hasil
    }
    return jsonify(message)

# max_thresh = 255
# thresh = 6
# image_make(thresh)
