from dataclasses import dataclass
from pysv.classes.color import Colors
from pysv.defaults import (
    DEFAULT_CL_S_KEY,
    DEFAULT_HELP_KEY,
    DEFAULT_LIST_KEY,
    DEFAULT_SHOW_KEY,
    DEFAULT_COLOR_SCM,
)


@dataclass
class Settings:
    color_scheme: Colors = DEFAULT_COLOR_SCM
    clear_key: str = DEFAULT_CL_S_KEY
    show_key: str = DEFAULT_SHOW_KEY
    list_key: str = DEFAULT_LIST_KEY
    help_key: str = DEFAULT_HELP_KEY
