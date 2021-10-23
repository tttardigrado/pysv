prompt_txt: list = [("class:prompt_text", ">>> ")]

bottom_toolbar: str = " PySV: A terminal app to help you with your CSV file"

help_msg_1: str = """Help

{load, ld:} Load a new csv file into memory
    (load «path_to_file|named_file»)
    (ld «path_to_file|named_file»)

{save, sv:} Save the currently loaded csv to a file
    (save «path_to_file|NONE»)

    (sv «path_to_file|NONE»)

{peek:} show a single column or row
    (peek «column|row» «name»)

{ls:} show the names of all column, rows or both
    (ls «column|row| »)

{delete, del:} delete all the values on a specified column or row
    (delete «column|row» «name»)
    (del «column|row» «name»)

{cell:} show the value of a specified cell
    (cell «column_name» «row_name»)

{copy, cp:} copy to the clipboard the contents of a specified cell
    (copy «column_name» «row_name»)
    (cp «column_name» «row_name»)

{switch, sw:} switch the values between two tables or two rows
    (switch «column|row» «name_1» | «name_2»)
    (sw «column|row» «name_1» | «name_2»)

{edit:} edit the content of a specified cell
    (edit «column_name» «row_name»)

{replace:} replace the content of a specified cell
    (replace «column_name» «row_name»)

{show, s:} show the current csv file as an html table inside a browser

{help, h:} show this message

{clear, cls, c:} clear the screen
"""

help_msg: str = (
    help_msg_1.replace("{", "<ansigreen>* ")
    .replace("}", "</ansigreen>")
    .replace("(", "<ansicyan>* ")
    .replace(")", "</ansicyan>")
)
