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
            self.k          = 3 if k is None or k <= 1 else k
            self.img_folder = "./vin/img/" if img_folder is None else img_folder

            # logging
            self.log_to_console = True if log_to_console is None else log_to_console
            self.log_to_file    = True if log_to_file is None else log_to_file
            self.logfile        = './vin.log' if logfile is None else logfile
            self.log_level      = 'DEBUG' if log_level is None else log_level

            # test
            self.test_k            = 3 if test_k is None else test_k
            self.test_img_folder   = "./test/img/" if test_img_folder is None else test_img_folder
            self.test_img_filename = "test_image.jpg" if test_img_filename is None else test_img_filename


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

    def __str__(self):
        return f'\
            k = {self.k}, img_folder = {self.img_folder}\
            log_to_console = {self.log_to_console}, log_to_file = {self.log_to_file}, logfile = {self.logfile}, log_level = {self.log_level},\
            test_k = {self.test_k}, test_img_folder = {self.test_img_folder}, test_img_filename = {self.test_img_filename}'
