from vin.vin_image import VinImage

from typing import List
import os
import logging


def cargar_imagenes(directorio: str) -> List[VinImage]:
    """Carga la estructura de imágenes, almacenada de la siguiente forma:
    ```
    img
    |-> clase1
    |      |-> archivo1.png
    |      |
    |      ...
    |-> clase2
    ...
    ```
    """
    imagenes = []

    for subcarpeta in os.scandir(directorio):
        for img in os.scandir(subcarpeta):
            if img.is_file:
                imagenes.append(VinImage(img.path, subcarpeta.name))

    return imagenes
