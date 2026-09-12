"""Config utilities."""

DEFAULT_CONFIG = {
    "debug": False,
    "timeout": 30,
    "max_retries": 3,
}


def get_config_value(config, key):
    if key not in config:
        return DEFAULT_CONFIG.get(key)

    return config[key]


def merge_config(custom_config):
    config = DEFAULT_CONFIG.copy()
    config.update(custom_config)

    return config