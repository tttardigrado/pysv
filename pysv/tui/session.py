from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts.dialogs import input_dialog
from pysv.defaults import DEFAULT_HISTORY_PATH
from pysv.functions.html import show_html_table
from pysv.creators.create_csv_file import load_csv
from pysv.functions.output import error_message, title_message
from pysv.classes.csv_file import CSVFile
from pysv.classes.settings import Settings
from pysv.creators.create_settings import make_settings
from pysv.functions.general import clear_screen, p_print
from pysv.tui.constants import prompt_txt, bottom_toolbar, help_msg
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style
from prompt_toolkit.history import FileHistory
import pyperclip
from typing import List, Tuple


class Session:
    """
    Prompt Toolkit Sessions that provides the TUI
    """

    def __init__(self) -> None:
        # load the settings
        self.settings: Settings = make_settings()
        # init the csv file
        self.csv: CSVFile = CSVFile([], [])
        # create the session
        self.session: PromptSession = self.make_session()
        # determine the SolRing toolbar text
        self.toolbar: str = bottom_toolbar
        # help message
        self.help_msg: str = help_msg

    def not_valid(self) -> None:
        """
        Function that prints a message when a command is not valid
        """
        p_print(error_message("Not a valid command!"))

    def no_csv(self) -> None:
        """
        Function that prints a message when a csv file has not been loaded
        """
        p_print(error_message("No «CSV file» has been loaded"))

    def select_rows(self) -> str:
        """
        Create a radio checkbox for the user to select the rows

        Returns:
            (str): the value chosen by the user
        """
        return radio(
            "Row",
            self.csv.make_row_num_list(),
            self.settings.color_scheme.render_style(),
        )

    def select_columns(self) -> str:
        """
        Create a radio checkbox for the user to select the columns

        Returns:
            (str): the value chosen by the user
        """
        return radio(
            "Column", self.csv.header, self.settings.color_scheme.render_style()
        )

    def run(self) -> None:
        """
        Run the prompt.
        A session prompt will be shown the resulting input will be processed
        """
        # create and show prompt
        text: str = self.session.prompt(
            prompt_txt, bottom_toolbar=self.toolbar, complete_while_typing=True
        )

        if text:
            # process the input
            try:
                if self.csv.is_loaded():
                    self.process_input(text)
                else:
                    self.process_input_no_csv(text)

            except Exception:
                self.not_valid()

    def make_session(self) -> PromptSession:
        """
        Setup prompt toolkit session for simple search

        Returns:
            PromptSession: session for simple search
        """
        completer: NestedCompleter = NestedCompleter.from_nested_dict(
            {
                "clear": None,
                "c": None,
                "help": None,
                "h": None,
                "load": None,
                "ld": None,
                "delete": {"column", "row"},
                "del": {"column", "row"},
                "peek": {"column", "row"},
                "show": None,
                "s": None,
                "ls": {"column", "row"},
                "cell": None,
                "copy": None,
                "cp": None,
                "edit": None,
                "replace": None,
                "switch": {"column", "row"},
                "sw": {"column", "row"},
            }
        )
        return PromptSession(
            completer=completer,
            complete_while_typing=True,
            history=FileHistory(DEFAULT_HISTORY_PATH),
            auto_suggest=AutoSuggestFromHistory(),
        )

    def process_input(self, command: str) -> None:
        """
        Process the input provided to the prompt

        Argumnets:
            command (str): command provided by the user that will be processed
        """

        # properly format the input
        commands: List[str] = command.split()
        first_word: str = commands[0].lower()

        if first_word in {"clear", "cls", "c"}:
            clear_screen()

        elif first_word in {"help", "h"}:
            p_print(help_msg)

        elif first_word in {"load", "ld"}:
            self.csv = load_csv(commands[1])

        elif first_word in {"delete", "del"}:
            msg: str = self.delete_function(commands)
            if msg:
                p_print(msg)
            else:
                self.not_valid()

        elif first_word == "peek":
            msg: str = self.peek_function(commands)
            if msg:
                p_print(msg)
            else:
                self.not_valid()

        elif first_word in {"show", "s"}:
            show_html_table(self.csv, self.settings)

        elif first_word == "ls":
            p_print(self.ls_function(commands))

        elif first_word == "cell":
            p_print(self.cell_function(commands)[0])

        elif first_word in {"copy", "cp"}:
            p_print(self.copy_function(commands))

        elif first_word in {"switch", "sw"}:
            msg: str = self.switch_function(commands)
            if msg:
                p_print(msg)
            else:
                self.not_valid()

        elif first_word == "edit":
            p_print(self.edit_function(commands, True))

        elif first_word == "replace":
            p_print(self.edit_function(commands))

        else:
            self.not_valid()

    def process_input_no_csv(self, command: str) -> None:
        """
        Process the input provided to the prompt

        Argumnets:
            command (str): command provided by the user that will be processed
        """

        # properly format the input
        commands: List[str] = command.split()
        first_word: str = commands[0].lower()

        if first_word in {"clear", "cls", "c"}:
            clear_screen()
        elif first_word in {"help", "h"}:
            p_print(help_msg)
        elif first_word in {"load", "ld"}:
            self.csv = load_csv(commands[1])
        else:
            self.no_csv()

    def cell_function(self, command: List[str]) -> Tuple[str, str]:
        try:
            # len == 1 -> commands == ["cell"]
            if len(command) == 1:
                raise IndexError

            # cell                  | Last Name Column      | 2          |
            return self.csv.get_cell(" ".join(command[1:-1]), command[-1])

        except IndexError:
            # select the column and the row using a radio checkbox
            col: str = self.select_columns()
            row: str = self.select_rows()
            return self.csv.get_cell(col, row)

    def edit_function(self, commands: List[str], to_copy: bool = False) -> str:
        try:
            # len == 1 -> commands == ["edit"] || ["change"]
            if len(commands) == 1:
                raise IndexError

            col: str = " ".join(commands[1:-1])
            row: str = commands[-1]

        except IndexError:
            # select the column and the row using a radio checkbox
            col: str = self.select_columns()
            row: str = self.select_rows()

        output, content = self.csv.get_cell(col, row)

        if content:
            title: str = f"{col} - {row}"
            if to_copy:
                pyperclip.copy(content)
                value: str = copied_input(
                    title, self.settings.color_scheme.render_style()
                )
            else:
                value: str = non_copied_input(
                    title, self.settings.color_scheme.render_style()
                )

            if value:
                was_set: bool = self.csv.set_cell(col, row, value)
                if was_set:
                    return title_message("Set to", value)
            return error_message("The value was not set!")

        else:
            return output

    def ls_function(self, commands: List[str]) -> str:
        try:
            if commands[1] == "column":
                return self.csv.list_columns()

            elif commands[1] == "row":
                return self.csv.list_rows()

            else:
                # list both
                return self.csv.list_col_and_rows()

        except IndexError:
            # a second parameter was not provided
            # list both
            return self.csv.list_col_and_rows()

    def peek_function(self, commands: List[str]) -> str:
        if commands[1] == "column":
            try:
                # peek column              | Last Name            |
                return self.csv.peek_column(" ".join(commands[2:]))

            except IndexError:
                # no column name was given
                # select a column
                col: str = self.select_columns()
                return self.csv.peek_column(col)

        elif commands[1] == "row":
            try:
                # peel row              | 1         |
                return self.csv.peek_row(commands[2])

            except IndexError:
                # no row number given
                # select a row
                row: str = self.select_rows()
                return self.csv.peek_row(row)
        else:
            return ""

    def copy_function(self, commands: List[str]) -> str:
        # get the values of the cell
        response: Tuple[str, str] = self.cell_function(commands)
        msg: str = response[0]
        to_copy: str = response[1]

        if to_copy:
            # copy
            pyperclip.copy(to_copy)
            return "<ansigreen>Copied</ansigreen>\n" + msg

        else:
            # don't copy
            return msg

    def switch_function(self, commands: List[str]) -> str:
        if commands[1] == "column":
            try:
                # try to get the columns: switch column col1 | col2
                cols: List[str] = " ".join(commands[2:]).split("|")
                col1: str = cols[0].strip()
                col2: str = cols[1].strip()
            except IndexError:
                # means at least one column was not provided
                # select columns 1 and 2
                col1: str = self.select_columns()
                col2: str = self.select_columns()

            # switch the columns and return the message
            return self.csv.switch_column(col1, col2)

        elif commands[1] == "row":
            try:
                # try to get the rows: switch row row1 | row2
                rows: List[str] = " ".join(commands[2:]).split("|")
                row1: str = rows[0].strip()
                row2: str = rows[1].strip()
            except IndexError:
                # means at least one of the rows was not provided
                # select rows 1 and 2
                row1: str = self.select_rows()
                row2: str = self.select_rows()

            # switch the rows and return the message
            return self.csv.switch_row(row1, row2)

        else:
            return ""

    def delete_function(self, commands: List[str]) -> str:
        try:
            if commands[1] == "column":
                try:
                    # delete column              | Last Name            |
                    return self.csv.delete_column(" ".join(commands[2:]))

                except IndexError:
                    # the column name was not provided
                    # select the column
                    col: str = self.select_columns()
                    return self.csv.delete_column(col)

            elif commands[1] == "row":
                try:
                    # delete row              | 2         |
                    return self.csv.delete_row(commands[2])

                except IndexError:
                    # the row name was not provided
                    # select the row
                    row: str = self.select_rows()
                    return self.csv.delete_row(row)

            else:
                return ""

        except IndexError:
            return ""


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
