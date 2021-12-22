import vin.modelo
import vin.file_io
from vin.vin_image import VinImage
from vin.pipeline import Pipeline
from vin.vin_config import VinConfig


import pytest
import toml
from os import path

config = VinConfig()


# ───────────────────────────────────────────────────────────────── FIXTURES ─────


@pytest.fixture
def imagen_test():
    return VinImage(config.test_img_folder + config.test_img_filename)


# ────────────────────────────────────────────────────────────────────────────────


def test_image_creation(imagen_test):
    imagen_test
    assert imagen_test != None


def test_image_downscale(imagen_test):
    resolucion: tuple[int, int] = (64, 64)

    imagen_test.downscale(resolucion)

    assert imagen_test.resolution() == resolucion


def test_image_tag(imagen_test):
    nuevo_tag = 'prueba!'
    imagen_test.change_tag(nuevo_tag)

    assert nuevo_tag == imagen_test.tag


def test_image_vectorization(imagen_test):
    features = imagen_test.extract_features()

    assert len(features) != 0, "La lista de caracerísticas está vacía"


def test_carga_imagenes():
    path = config.img_folder
    lista = vin.file_io.cargar_imagenes(path)

    assert len(lista) != 0, "No se han cargado correctamente las imágenes"


def test_knn(imagen_test):
    dataset = vin.file_io.cargar_imagenes(config.img_folder)

    k = config.k

    tag = vin.modelo.knn(imagen_test, dataset, k)

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
    logger.critical("Mensaje de error crítico")

    # Comprobar que se crea el archivo de logging
    from datetime import datetime


    now = datetime.now()
    salida = "Testing logging file (" + now.strftime("%Y/%m/%d, %H:%M:%S") + ")"

    log_config.log_to_file = True
    logger = LoggerConfig.get(log_config)

    logger.debug(salida)

    assert path.exists(log_config.logfile)
    assert open(log_config.logfile, 'r').read().find(salida) != -1

    assert logger != None