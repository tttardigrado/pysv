from os import system, path, makedirs
from prompt_toolkit import print_formatted_text, HTML
from pysv.defaults import (
    DEFAULT_CONFIG_DIR,
    DEFAULT_HISTORY_PATH,
    DEFAULT_SETTINGS_PATH,
)


def clear_screen() -> None:
    """
    Utility function for clearing the console screen.
    """
    _ = system("clear")


def p_print(text: str) -> None:
    print_formatted_text(HTML(text))


def make_file(path_to_file: str) -> None:
    if not path.exists(path_to_file):
        with open(path_to_file, "w") as _:
            pass


def make_config() -> None:
    if not path.exists(DEFAULT_CONFIG_DIR):
        makedirs(DEFAULT_CONFIG_DIR)

    make_file(DEFAULT_HISTORY_PATH)
    make_file(DEFAULT_SETTINGS_PATH)
