import vin.modelo
import vin.file_io
from vin.vin_image import VinImage
from vin.pipeline import Pipeline
from vin.vin_config import VinConfig


import pytest
import toml
from os import path

config = VinConfig()

def test_image_creation():
    path = config.test_img_folder + config.test_img_filename
    imagen = VinImage(path)
    assert imagen != None

def test_image_downscale():
    resolucion: tuple[int, int] = (64, 64)
    path = config.test_img_folder + config.test_img_filename

    imagen = VinImage(path)
    imagen.downscale(resolucion)

    assert imagen.resolution() == resolucion

def test_image_tag():
    path = config.test_img_folder + config.test_img_filename
    imagen = VinImage(path)

    nuevo_tag = 'prueba!'
    imagen.change_tag(nuevo_tag)

    assert nuevo_tag == imagen.tag


def test_image_vectorization():
    path = config.test_img_folder + config.test_img_filename
    imagen = VinImage(path)

    features = imagen.extract_features()

    assert len(features) != 0, "La lista de caracerísticas está vacía"

def test_carga_imagenes():
    path = config.img_folder
    lista = vin.file_io.cargar_imagenes(path)

    assert len(lista) != 0, "No se han cargado correctamente las imágenes"

def test_knn():
    dataset = vin.file_io.cargar_imagenes(config.img_folder)

    path = config.test_img_folder + config.test_img_filename
    imagen = VinImage(path)

    k = config.k

    tag = vin.modelo.knn(imagen, dataset, k)

    assert tag != 'unknown', "No se ha creado correctamente la etiqueta en knn"

# ────────────────────────────────────────────────────────────────────────────────

def test_pipeline_creation():
    pipeline = Pipeline()
    assert pipeline != None


def test_config():
    config = VinConfig()
    default_k = config.test_k

    k = 5
    config = VinConfig(test_k = k)

    assert config.test_k != default_k and config.test_k == k


def test_config_path():
    config = VinConfig(path = VinConfig.default_config_file)

    assert path.exists(VinConfig.default_config_file)
    assert config != None


def test_logger():
    from vin.logger import LoggerConfig

    log_config = VinConfig(log_to_file=False)

    logger = LoggerConfig.get(log_config)

    logger.debug("Mensaje de debug")
    logger.info("Mensaje de info")
    logger.success("Mensaje de success")
    logger.warning("Mensaje de warning")
    logger.error("Mensaje de error")
    logger.critical("Mensajde de error crítico")

    assert logger != None