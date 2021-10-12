import webbrowser
from pysv.defaults import DEFAULT_CSS_STR
from pysv.classes.settings import Settings
from pysv.classes.csv_file import CSVFile


def html_boilerplate(style: str, table: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSV</title>
<style>
{style}
</style>
</head>
<body>
{table}
</body>
</html>"""


def css_boilerplate(settings: Settings, css_string: str) -> str:
    """
    Generate the CSS for the CSV as HTML table viewer

    Arguments:
        settings (Settings): Settings object containing (at least)
            the color scheme for the css
        css_string (str): a string containing the styles for the html table

    Returns:
        (str): full css (including the varibales and the styles)
    """
    # concat variables ------------------------ and -- styles
    return settings.color_scheme.render_css() + "\n" + css_string


def output_html(
    file: CSVFile, settings: Settings, css_string: str = DEFAULT_CSS_STR
) -> str:
    """
    Generate/Render the html that shows a CSV file as an html table

    Arguments:
        file (CSVFile): CSV Object that contains:
            * The header of the CSV (columns)
            * A list of all the other rows
        settings (Settings): Settings object containing (at least)
            the color scheme for the css
        css_string (str): a string containing the styles for the html table

    Returns:
        (str): The html string
    """
    # get the table html
    table_content: str = file.make_table_str()

    # get the css
    css: str = css_boilerplate(settings, css_string)

    # add the html boilerplate to generate the final string
    return html_boilerplate(css, table_content)


def show_html_table(
    file: CSVFile, settings: Settings, css_string: str = DEFAULT_CSS_STR
) -> None:
    """
    Open a CSV file as a html table using the default system browser

    Arguments:
        file (CSVFile): CSV Object that contains:
            * The header of the CSV (columns)
            * A list of all the other rows
        settings (Settings): Settings object containing (at least)
            the color scheme for the css
        css_string (str): a string containing the styles for the html table
    """
    # path to the tmp (temporary) file to store the html output
    file_name: str = "/tmp/table.html"

    # create or override the tmp file
    with open(file_name, "w") as f:
        # generate and write the html
        f.write(output_html(file, settings, css_string))

    # open the tmp html file using the default system browser
    webbrowser.open_new_tab(file_name)
