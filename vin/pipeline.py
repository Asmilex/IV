from vin.vin_image import VinImage
import vin.logger
from vin.vin_config import VinConfig


logger = vin.logger.logger

class Pipeline:
    def __init__(self):
        logger.info("Inicializando pipeline")

        logger.info('Procesando imagen')
        self.preprocesar(None)

        logger.info('Etiquetando imagen')
        self.etiquetar(None)

        logger.info('Almacenando imagen')
        self.almacenar_imagen(None)


    def preprocesar(self, imagen: VinImage):
        pass


    def etiquetar(self, imagen: VinImage):
        pass


    def almacenar_imagen(self, imagen: VinImage):
        pass
