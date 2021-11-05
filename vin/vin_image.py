import cv2 as cv
from typing import Tuple

class VinImage:
    def __init__(self, file_path: str, tag='unknown'):
        self.image = cv.imread(file_path)
        self.tag = tag

    def change_tag(self, nuevo_tag: str):
        self.tag = nuevo_tag

    def resolution(self) -> Tuple[int, int]:
        return (self.image.shape[0], self.image.shape[1])

    def downscale(self, resolucion: Tuple[int, int]):
        self.image = cv.resize(self.image, resolucion, interpolation=cv.INTER_AREA)


    # ─────────────────────────────────────────────────────── ESPACIO DE COLORES ─────


    def grayscale(self):
        return cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

    def hsv(self):
        return cv.cvtColor(self.image, cv.COLOR_BGR2HSV)


    # ──────────────────────────────────────────── EXTRACCION DE CARACTERISTICAS ─────


    def hu_moments(self):
        features = cv.HuMoments(cv.moments(self.grayscale()))
        return features.flatten().tolist()

    def histogram(self):
        size = 32
        hist = cv.calcHist(
            images   = [self.hsv()],
            channels = [0, 1, 2],
            mask     = None,
            ranges   = [0, 256, 0, 256, 0, 256],
            histSize = [size, size, size]
        )
        cv.normalize(hist, hist)
        return hist.flatten().tolist()

    def extract_features(self):
        features = self.hu_moments() + self.histogram()
        return features