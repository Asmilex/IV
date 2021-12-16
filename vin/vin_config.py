import toml

class VinConfig:
    default_config_file = './vin_config.toml'

    def __init__(self, path = None,
        k = None, img_folder = None,
        log_to_console = None, log_to_file = None, logfile = None, log_level = None,
        test_k = None, test_img_folder = None, test_img_filename = None
    ):
        if path:
            self.load(path)
        else:
            # Vin
            self.k          = k if k else 3
            self.img_folder = img_folder if img_folder else "./vin/img/"

            # logging
            self.log_to_console = log_to_console if log_to_console else True
            self.log_to_file    = log_to_file if log_to_file else True
            self.logfile        = logfile if logfile else './vin.log'
            self.log_level      = log_level if log_level else 'DEBUG'

            # test
            self.test_k            = test_k if test_k else 3
            self.test_img_folder   = test_img_folder if test_img_folder else "./test/img/"
            self.test_img_filename = test_img_filename if test_img_filename else "test_image.jpg"


    def load(self, path):
        config = toml.load(path)

        # Vin
        self.k          = config['vin']['k']
        self.img_folder = config['vin']['img_folder']

        # logging
        self.log_to_console = config['logging']['log_to_console']
        self.log_to_file    = config['logging']['log_to_file']
        self.logfile        = config['logging']['logfile']
        self.log_level      = config['logging']['log_level']

        # test
        self.test_k            = config['test']['k']
        self.test_img_folder   = config['test']['img_folder']
        self.test_img_filename = config['test']['img_filename']
