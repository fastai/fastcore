# Copyright © 2016-2021 Scott Stevenson <scott@stevenson.io>
# Modifications copyright © 2022 onwards Jeremy Howard

"""XDG Base Directory Specification variables.

xdg_cache_home(), xdg_config_home(), xdg_data_home(), and xdg_state_home()
return pathlib.Path objects containing the value of the environment variable
named XDG_CACHE_HOME, XDG_CONFIG_HOME, XDG_DATA_HOME, and XDG_STATE_HOME
respectively, or the default defined in the specification if the environment
variable is unset, empty, or contains a relative path rather than absolute
path.

xdg_config_dirs() and xdg_data_dirs() return a list of pathlib.Path
objects containing the value, split on colons, of the environment
variable named XDG_CONFIG_DIRS and XDG_DATA_DIRS respectively, or the
default defined in the specification if the environment variable is
unset or empty. Relative paths are ignored, as per the specification.

xdg_runtime_dir() returns a pathlib.Path object containing the value of
the XDG_RUNTIME_DIR environment variable, or None if the environment
variable is not set, or contains a relative path rather than absolute path.
"""

import os
from pathlib import Path
from typing import List, Optional

__all__ = [ "xdg_cache_home", "xdg_config_dirs", "xdg_config_home", "xdg_data_dirs", "xdg_data_home", "xdg_runtime_dir", "xdg_state_home",
    "XDG_CACHE_HOME", "XDG_CONFIG_DIRS", "XDG_CONFIG_HOME", "XDG_DATA_DIRS", "XDG_DATA_HOME", "XDG_RUNTIME_DIR" ]


def _path_from_env(variable: str, default: Path) -> Path:
    value = os.environ.get(variable)
    if value and os.path.isabs(value): return Path(value)
    return default

def _paths_from_env(variable: str, default: List[Path]) -> List[Path]:
    value = os.environ.get(variable)
    if value:
        paths = [ Path(path) for path in value.split(":") if os.path.isabs(path) ]
        if paths: return paths
    return default

def xdg_cache_home() -> Path:
    """Path corresponding to XDG_CACHE_HOME."""
    return _path_from_env("XDG_CACHE_HOME", Path.home()/".cache")

def xdg_config_dirs() -> List[Path]:
    """Paths corresponding to XDG_CONFIG_DIRS."""
    return _paths_from_env("XDG_CONFIG_DIRS", [Path("/etc/xdg")])

def xdg_config_home() -> Path:
    """Path corresponding to XDG_CONFIG_HOME."""
    return _path_from_env("XDG_CONFIG_HOME", Path.home()/".config")

def xdg_data_dirs() -> List[Path]:
    """Paths corresponding to XDG_DATA_DIRS."""
    return _paths_from_env( "XDG_DATA_DIRS", [Path(path) for path in "/usr/local/share/:/usr/share/".split(":")])

def xdg_data_home() -> Path:
    """Path corresponding to XDG_DATA_HOME."""
    return _path_from_env("XDG_DATA_HOME", Path.home()/".local"/"share")

def xdg_runtime_dir() -> Optional[Path]:
    """Path corresponding to XDG_RUNTIME_DIR. """
    value = os.getenv("XDG_RUNTIME_DIR")
    return Path(value) if value and os.path.isabs(value) else None

def xdg_state_home() -> Path:
    """Path corresponding to XDG_STATE_HOME."""
    return _path_from_env("XDG_STATE_HOME", Path.home()/".local"/"state")

