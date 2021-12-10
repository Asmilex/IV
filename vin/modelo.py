from vin.vin_image import VinImage
from vin.utils import distancia
from typing import List


def knn(imagen: VinImage, dataset: List[VinImage], k: int) -> str:
    """Aproxima `imagen` a los `k` vecinos más próximos utilizando las imágenes presentes en `dataset`"""

    tag = "unknown"

    # Preparamos ambas entradas: tanto la imagen a aproximar como el modelo
    dataset_features = [img.extract_features() for img in dataset]
    img_features = imagen.extract_features()

    # Calculamos las distancias a los elementos del espacio. Estamos buscando las `k` imágenes más cercanas
    distancias = []

    for v in dataset_features:
        distancias.append(distancia(img_features, v))

    # Necesitamos ver quién se ha quedado más cerca. Para ello, intentamos ordenar las distancias de menor a mayor, y vemos qué imágenes se han quedado más cerca.
    distancias, dataset_ordenado = zip(*sorted(zip(distancias, dataset)))

    # Mirar las claves que hay en dataset por orden. Ir haciendo recuento, y quedarnos con la mayoritaria
    recuento = {}
    for i in range(k):
        tag = dataset_ordenado[i].tag

        if tag not in recuento:
            recuento[tag] = 1
        else:
            recuento[tag] = recuento[tag] + 1

    tag = max(recuento, key=recuento.get)

    return tag
