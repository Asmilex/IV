from vin.vin_image import VinImage
from vin.logger import LoggerConfig
from vin.vin_config import VinConfig

class Pipeline:
    def __init__(self):
        logger = LoggerConfig.get()
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
