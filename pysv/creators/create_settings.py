import os
import json
from pysv.classes.named_files import NamedFiles
from pysv.functions.output import error_message
from pysv.functions.general import p_print
from pysv.defaults import DEFAULT_CL_S_KEY, DEFAULT_HELP_KEY, DEFAULT_LIST_KEY
from pysv.classes.settings import Settings
from pysv.classes.color import Colors
from pysv.creators.create_color import make_color_scheme


def make_settings(path: str = "~/.config/pysv/config.json") -> Settings:
    try:
        with open(os.path.expanduser(path), "r") as s:
            data: dict = json.load(s)
    except (FileNotFoundError, json.JSONDecodeError):
        p_print(error_message("There's no settings file!", title="Warning"))
        return Settings()

    scheme: Colors = make_color_scheme(data)
    files: NamedFiles = NamedFiles(files=data.get("named_files") or {})
    clear_key: str = data.get("clear_key") or DEFAULT_CL_S_KEY
    list_key: str = data.get("list_key") or DEFAULT_LIST_KEY
    help_key: str = data.get("help_key") or DEFAULT_HELP_KEY

    return Settings(
        named_files=files,
        color_scheme=scheme,
        clear_key=clear_key,
        list_key=list_key,
        help_key=help_key,
    )
