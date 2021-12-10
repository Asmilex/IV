import vin.modelo
import vin.file_io
from vin.vin_image import VinImage
from vin.pipeline import Pipeline

import pytest
import toml

config = toml.load('./vin_config.toml')

def test_image_creation():
    path = config['test']['img_folder'] + config['test']['img_filename']
    imagen = VinImage(path)
    assert imagen != None

def test_image_downscale():
    resolucion: tuple[int, int] = (64, 64)
    path = config['test']['img_folder'] + config['test']['img_filename']

    imagen = VinImage(path)
    imagen.downscale(resolucion)

    assert imagen.resolution() == resolucion

def test_image_tag():
    path = config['test']['img_folder'] + config['test']['img_filename']
    imagen = VinImage(path)

    nuevo_tag = 'prueba!'
    imagen.change_tag(nuevo_tag)

    assert nuevo_tag == imagen.tag


def test_image_vectorization():
    path = config['test']['img_folder'] + config['test']['img_filename']
    imagen = VinImage(path)

    features = imagen.extract_features()

    assert len(features) != 0, "La lista de caracerísticas está vacía"

def test_carga_imagenes():
    path = config['vin']['img_folder']
    lista = vin.file_io.cargar_imagenes(path)

    assert len(lista) != 0, "No se han cargado correctamente las imágenes"

def test_knn():
    dataset = vin.file_io.cargar_imagenes(config['vin']['img_folder'])

    path = config['test']['img_folder'] + config['test']['img_filename']
    imagen = VinImage(path)

    k = config['test']['k']

    tag = vin.modelo.knn(imagen, dataset, k)

    assert tag != 'unknown', "No se ha creado correctamente la etiqueta en knn"

# ────────────────────────────────────────────────────────────────────────────────

def test_pipeline_creation():
    pipeline = Pipeline()

    assert pipeline != None