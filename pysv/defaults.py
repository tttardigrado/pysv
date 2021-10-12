from pysv.classes.color import Colors
from os import path

# Default key binding to CLear the Screen
DEFAULT_CL_S_KEY: str = "m-c"

# Default key binding to list all rows and columns
DEFAULT_LIST_KEY: str = "m-l"

# Default key binding to show the help message
DEFAULT_HELP_KEY: str = "m-h"

# Default key binding to show the csv as an html table
DEFAULT_SHOW_KEY: str = "m-s"

# Nord color scheme
NORD: Colors = Colors(
    bg_color="#2e3440",
    border_color="#4c566a",
    title_color="#5e81ac",
    text_color_1="#c2c8d3",
    text_color_2="#81a1c1",
)

# Gruvbox color scheme
GRUVBOX: Colors = Colors(
    bg_color="#1d2021",
    border_color="#3c3836",
    title_color="#458588",
    text_color_1="#83a598",
    text_color_2="#d3869b",
)

# Dracula color scheme
DRACULA: Colors = Colors(
    bg_color="#282a36",
    border_color="#44475a",
    title_color="#ff79c6",
    text_color_1="#8be9fd",
    text_color_2="#ab86e2",
)

# Monokai color scheme
MONOKAI: Colors = Colors(
    bg_color="#2c292d",
    border_color="#908e8f",
    title_color="#ab9df2",
    text_color_1="#a9dc76",
    text_color_2="#78dce8",
)

# Palenight color scheme
PALENIGHT: Colors = Colors(
    bg_color="#282a36",
    border_color="#44475a",
    title_color="#ff79c6",
    text_color_1="#8be9fd",
    text_color_2="#67d5f5",
)

# Default Color scheme name
DEFAULT_COLOR_SCM: Colors = NORD

DEFAULT_CSS_STR: str = """
body {
  background-color: var(--bg-color);
  font-family: "Fira Code", monospace;
  font-size: 1.5rem;
  font-weight: 500;
  color: var(--text-color);
}

table {
  border-collapse: collapse;
}

table, th, td {
  border: 3px solid var(--border-color);
}

th, td {
  padding: 0.4rem 1rem;
  text-align: left;
}

th {
  color: var(--title-color);
}

tr:nth-child(even) {
  color: var(--text-color-2);
}
"""

# paths for the configuration files
DEFAULT_CONFIG_DIR = path.expanduser("~/.config/pysv")
DEFAULT_HISTORY_PATH = path.join(DEFAULT_CONFIG_DIR, ".pysvhistory")
DEFAULT_SETTINGS_PATH = path.join(DEFAULT_CONFIG_DIR, "config.json")
