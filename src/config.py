"""Config utilities."""


DEFAULT_CONFIG = {
    "log_level": "INFO",
    "cache_enabled": True,
    "log_format": "%(levelname)s:%(message)s",
    "feature_enabled": False,
    "debug": False,
    "timeout": 30,
    "max_retries": 3,
    "environment": "development",
}


def get_config_value(key: str):
    return DEFAULT_CONFIG.get(key)


def merge_config(overrides: dict) -> dict:
    config = DEFAULT_CONFIG.copy()
    config.update(overrides)
    return config

def copy_config(config: dict) -> dict:
    return config.copy()
