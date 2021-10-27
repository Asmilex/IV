import cv2 as cv
from typing import Tuple

class VinImage:
    def __init__(self, file_path: str):
        self.image = cv.imread(file_path)
        self.tag = 'unknown'    # Correspondiente a la carpeta en la que se encuentra.

    def change_tag(self, nuevo_tag: str):
        self.tag = nuevo_tag

    def resolution(self) -> Tuple[int, int]:
        return (self.image.shape[0], self.image.shape[1])

    def downscale(self, resolucion: Tuple[int, int]):
        self.image = cv.resize(self.image, resolucion, interpolation=cv.INTER_AREA)

    def grayscale(self):
        return cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

    def hsv(self):
        return cv.cvtColor(self.image, cv.COLOR_BGR2HSV)