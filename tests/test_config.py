from src.config import (
    DEFAULT_CONFIG,
    get_config_value,
    merge_config,

    copy_config,)


def test_default_timeout():
    assert DEFAULT_CONFIG["timeout"] == 30


def test_default_debug():
    assert DEFAULT_CONFIG["debug"] is False


def test_default_environment():
    assert DEFAULT_CONFIG["environment"] == "development"


def test_get_timeout():
    assert get_config_value("timeout") == 30


def test_get_debug():
    assert get_config_value("debug") is False


def test_get_environment():
    assert get_config_value("environment") == "development"


def test_merge_config():
    result = merge_config(
        {"timeout": 60}
    )

    assert result["timeout"] == 60

def test_feature_enabled_config():
    assert get_config_value("feature_enabled") is False

def test_log_format_config():
    assert (
        get_config_value("log_format")
        == "%(levelname)s:%(message)s"
    )

def test_copy_config():
    original = {"timeout": 30}
    copied = copy_config(original)

    assert copied == original
    assert copied is not original

def test_cache_enabled_config():
    assert get_config_value("cache_enabled") is True

def test_log_level_config():
    assert get_config_value("log_level") == "INFO"

def test_api_url_config():
    assert (
        get_config_value("api_url")
        == "https://api.example.com"
    )
