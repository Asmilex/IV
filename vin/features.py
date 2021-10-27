from vin.vin_image import VinImage
import cv2 as cv
import numpy as np

def hu_moments(imagen: VinImage):
    features = cv.HuMoments(cv.moments(imagen.grayscale()))
    return features.flatten()

def histogram(imagen: VinImage):
    size = 32
    hist = cv.calcHist(
        images   = [imagen.hsv()],
        channels = [0, 1, 2],
        mask     = None,
        ranges   = [0, 256, 0, 256, 0, 256],
        histSize = [size, size, size]
    )
    cv.normalize(hist, hist)
    return hist.flatten()

def extract_features(image: VinImage):
    features = np.hstack([hu_moments(image), histogram(image)])
    return features