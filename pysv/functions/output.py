def add_color(message: str, color: str) -> str:
    """
    Make text surrounded by «» with the provided color

    Arguments:
        message (str): message in which the text should be colored
        color (str): ansi color with which the text should be surrounded by.

    Returns:
        (str): formated (and surrounded by colors) text
    """
    return message.replace("«", f"<ansi{color}>").replace("»", f"</ansi{color}>")


def title_message(title: str, body: str, color: str = "green") -> str:
    """
    Generate a message that contains a title.

    Arguments:
        title (str): title for the message
        body (str): content of the message
        color (str): ansi color for the title and for
            every part of the body surrounded by «». Default "green".

    Returns:
        (str): formated message
    """
    # make text surrounded by «» colorfull
    body = add_color(body, color)
    return f"<ansi{color}>{title}</ansi{color}>: {body}"


def error_message(body: str, color: str = "red", title: str = "Error") -> str:
    """
    Generate an error message

    Arguments:
        body (str): content of the message
        color (str): ansi color for the "Error" and for
            every part of the body surrounded by «». Default "red".
        title (str): title for the error message. Default "Error"

    Returns:
        (str): formated message
    """
    # make text surrounded by «» colorfull
    body = add_color(body, color)
    return f"<ansi{color}>{title}</ansi{color}>: {body}"
