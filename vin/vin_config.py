import toml

class VinConfig:
    def load(path = './vin_config.toml', override = None):
        config = toml.load(path)

        if override:
            config.update(override)

        return config

    def override(config, override):
        config.update(override)
        return config