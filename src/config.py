"""Config utilities."""


DEFAULT_CONFIG = {
    "request_timeout": 15,
    "api_url": "https://api.example.com",
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
    """Return a configuration value by key."""
    return DEFAULT_CONFIG.get(key)


def merge_config(overrides: dict) -> dict:
    config = DEFAULT_CONFIG.copy()
    config.update(overrides)
    return config

def copy_config(config: dict) -> dict:
    return config.copy()

def validate_config(config: dict) -> bool:
    if not isinstance(config.get("debug"), bool):
        return False

    if not isinstance(config.get("timeout"), int):
        return False

    if config["timeout"] < 0:
        return False

    if not isinstance(config.get("max_retries"), int):
        return False

    if config["max_retries"] < 0:
        return False

    if not isinstance(
        config.get("environment"),
        str,
    ):
        return False

    return True

def get_required_config(key: str):
    if key not in DEFAULT_CONFIG:
        raise KeyError(
            f"Missing required configuration: {key}"
        )

    return DEFAULT_CONFIG[key]
