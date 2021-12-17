from vin.vin_image import VinImage
from vin.logger import logger
from vin.vin_config import VinConfig

class Pipeline:
    def __init__(self):
        self.logger = logger

        self.logger.info("Inicializando pipeline")

    def preprocesar(imagen: VinImage):
        pass


    def etiquetar(imagen: VinImage):
        pass

    def almacenar_imagen(imagen: VinImage):
        pass

pipeline = Pipeline()
