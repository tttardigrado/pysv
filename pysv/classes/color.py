from dataclasses import dataclass

from prompt_toolkit.styles.style import Style


@dataclass
class Colors:
    """
    Colors for the html renderer.
    """

    bg_color: str  # background
    border_color: str  # table border
    title_color: str  # <th>
    text_color_1: str  # even <td>
    text_color_2: str  # odd <td>

    def render_css(self) -> str:
        """
        Render this Color class as css :root variables

        Returns:
            (str): css root element -> :root{...}
        """
        return f"""
:root {{
    --bg-color: {self.bg_color};
    --border-color: {self.border_color};
    --title-color: {self.title_color};
    --text-color: {self.text_color_1};
    --text-color-2: {self.text_color_2};
}}
        """

    def render_style(self) -> Style:
        return Style.from_dict(
            {
                "dialog": f"bg: {self.bg_color}",
                "dialog.body": f"bg: {self.bg_color} {self.text_color_1}",
                "checkbox-checked": f"bg: {self.text_color_2}",
                "radio-checked": f"fg: {self.text_color_2}",
                "frame": f"bg: {self.border_color}",
                "button.focused": f"bg: {self.text_color_2}",
                "frame.label": f"bg: {self.title_color}",
                "prompt_text": f"fg: {self.text_color_2}",
                "text-area": f"bg: {self.bg_color} {self.text_color_2}",
            }
        )
