from prompt_toolkit.shortcuts import input_dialog, radiolist_dialog
from prompt_toolkit.styles import Style
from typing import List


def radio(title: str, options: List[str], style: Style) -> str:
    final_op: list = []
    for op in options:
        final_op.append((op, op))

    return radiolist_dialog(
        title=f"Choose a {title}", values=final_op, style=style
    ).run()


def copied_input(title: str, style: Style) -> str:
    return input_dialog(
        title=title,
        text="To edit the content of the cell press the Paste key",
        style=style,
    ).run()


def non_copied_input(title: str, style: Style) -> str:
    return input_dialog(
        title=title, text="Type the new cell content:", style=style
    ).run()
