from pysv.defaults import NORD, GRUVBOX, DRACULA, MONOKAI, PALENIGHT, DEFAULT_COLOR_SCM
from pysv.classes.color import Colors


def make_color_scheme(color_data: dict) -> Colors:
    """
    Retern the color scheme specified in the dict

    Arguments:
        color_data (dict): dictionary containing the colorsheme settings

    Returns:
        (Colors): Colors class object for the color scheme. Default NORD
    """
    # Name of the scheme
    try:
        # try to get the name
        color_scheme_name: str = color_data["colorScheme"].lower()
    except KeyError:
        # on error returns the default color scheme
        return DEFAULT_COLOR_SCM

    # check if the name is the name of a known color scheme
    if color_scheme_name == "gruvbox":
        return GRUVBOX
    elif color_scheme_name == "dracula":
        return DRACULA
    elif color_scheme_name == "monokai":
        return MONOKAI
    elif color_scheme_name == "palenight":
        return PALENIGHT
    elif color_scheme_name == "nord":
        return NORD
    elif color_scheme_name == "custom":
        # custom color scheme
        try:
            # get the colors for the custom color scheme
            colors: dict = color_data["colors"]
            # return the Custom color object
            return Colors(
                bg_color=colors["bg"],
                border_color=colors["border"],
                title_color=colors["title"],
                text_color_1=colors["text1"],
                text_color_2=colors["text2"],
            )
        except KeyError:
            # on error return the defaulr color scheme
            return DEFAULT_COLOR_SCM
    else:
        # default
        return DEFAULT_COLOR_SCM
