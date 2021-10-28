import vin.modelo
from vin.vin_image import VinImage
import vin.features
import pytest
import numpy as np

def test_image_creation():
    imagen = VinImage('./test/img/test_image.jpg')
    assert imagen != None

def test_image_downscale():
    resolucion: tuple[int, int] = (64, 64)
    imagen = VinImage('./test/img/test_image.jpg')
    imagen.downscale(resolucion)
    assert imagen.resolution() == resolucion

def test_image_tag():
    imagen = VinImage('./test/img/test_image.jpg')
    nuevo_tag = 'prueba!'
    imagen.change_tag(nuevo_tag)
    assert nuevo_tag == imagen.tag


def test_image_vectorization():
    imagen = VinImage('./test/img/test_image.jpg')
    features = vin.features.extract_features(imagen)
    assert(np.isfinite(features).all())

def test_carga_imagenes():
    path = './vin/img'
    lista = vin.modelo.cargar_imagenes(path)
    assert(len(lista) > 0)

def test_knn():
    path = './vin/img'
    imagen = VinImage('./test/img/test_image.jpg')
    dataset = vin.modelo.cargar_imagenes(path)
    k = 1
    tag = vin.modelo.knn(imagen, dataset, 1)
    assert(tag != '')
