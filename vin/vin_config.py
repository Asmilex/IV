import toml

class VinConfig:
    def __init__(self, path = './vin_config.toml'):
        config = toml.load(path)
        return config