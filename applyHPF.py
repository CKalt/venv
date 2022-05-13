import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]])

kernel_5x5 = np.array([
        [-1, -1, -1, -1, -1],
        [-1, 1, 2, 1, -1],
        [],
    ])
