from vin.features import extract_features
from vin.vin_image import VinImage
import os
import numpy as np

def cargar_imagenes(directorio: str) -> list[VinImage]:
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

    categorias = os.listdir(directorio)

    print("Comienza la carga de imágenes...")
    for subcarpeta in os.scandir(directorio):
        print(f'\t→ Cargando categoría {subcarpeta.name}')
        for img in os.scandir(subcarpeta):
            if (img.is_file):
                imagenes.append(
                    VinImage(img.path)
                )

    print("Listo ✓")
    return imagenes


def knn(imagen: VinImage, dataset: list[VinImage], k: int) -> str:
    """Aproxima `imagen` a los `k` vecinos más próximos utilizando las imágenes presentes en `dataset`
    """

    tag = 'unknown'

    # Preparamos ambas entradas: tanto la imagen a aproximar como el modelo
    dataset_features = []

    for img in dataset:
        dataset_features.append(extract_features(img))

    img_features = extract_features(imagen)


    # Calculamos las distancias a los elementos del espacio. Estamos buscando las `k` imágenes más cercanas
    distancias = []

    for v in img_features:
        distancias.append(
            np.linalg.norm(v - img_features)
        )
    distancias = np.array(distancias)

    # Necesitamos ver quién se ha quedado más cerca. Para ello, intentamos ordenar las distancias de menor a mayor, y vemos qué imágenes se han quedado más cerca.
    indices_ordenados = np.lexsort([distancias, dataset])


    #dataset_ordenado = dataset[indices_ordenados]


    return tag
