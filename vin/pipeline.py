from vin.vin_image import VinImage
from vin.logger import Logger
from vin.vin_config import VinConfig

class Pipeline:
    def __init__(self):
        self.logger = Logger()

        self.logger.info("Hola!")

    def preprocesar(imagen: VinImage):
        pass


    def etiquetar(imagen: VinImage):
        pass

    def almacenar_imagen(imagen: VinImage):
        pass

pipeline = Pipeline()
