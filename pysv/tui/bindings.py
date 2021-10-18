from pysv.classes.settings import Settings
from prompt_toolkit.key_binding import KeyBindings
from pysv.tui.constants import help_msg
from pysv.functions.general import p_print, clear_screen


def make_bindings(settings: Settings) -> KeyBindings:
    """
    Generate the key bindings object for the Prompt session

    Arguments:
        settings (Settings): Settings object containing at least:
            -> help_key
            -> clear_key
            -> list_key
            -> named_files

    Returns:
        (KeyBindings): Key bindings object for the prompt
    """

    # help key (default is h)
    h: str = settings.help_key

    # clear key (default is c)
    c: str = settings.clear_key

    # list key (default is l)
    l: str = settings.list_key

    bindings = KeyBindings()

    @bindings.add("escape", h)
    def _(event):
        """ Print the help message """
        p_print(help_msg)
        event.cli.renderer.erase()

    @bindings.add("escape", c)
    def _(event):
        """ Clear the screen """
        clear_screen()
        event.cli.renderer.erase()

    @bindings.add("escape", l)
    def _(event):
        """ List the named_files """
        p_print(settings.named_files.render())
        event.cli.renderer.erase()

    return bindings
