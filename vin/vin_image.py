from PIL import Image
from typing import Tuple

class VinImage:
    def __init__(self, file_path: str):
        self.image = Image.open(file_path)
        self.tag = 'unknown'    # Correspondiente a la carpeta en la que se encuentra.

    def change_tag(self, nuevo_tag: str):
        self.tag = nuevo_tag

    def resolution(self) -> Tuple[int, int]:
        return self.image.size

    def downscale(self, resolucion: Tuple[int, int]):
        self.image = self.image.resize(resolucion)