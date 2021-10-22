from vin.vin_image import VinImage

def cargar_imagenes() -> list(VinImage):
    """
    Carga la estructura de imágenes, almacenada de la siguiente forma:
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
    pass

def knn(imagen: VinImage, dataset: list(VinImage), k: int) -> str:
    """
    Aproxima `imagen` a los `k` vecinos más próximos utilizando las imágenes presentes en `dataset`
    """

    pass
