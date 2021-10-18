from dataclasses import dataclass, field
from pysv.functions.output import error_message


@dataclass
class NamedFiles:
    files: dict = field(default_factory=dict)

    def render(self) -> str:
        msg: str = ""
        for name, path in self.files.items():
            msg += f"<ansigreen>{name}:</ansigreen> {path}\n"

        if msg == "":
            return error_message("There are no «Named Files»")

        return msg

    def get_file(self, name: str, default: str) -> str:
        return self.files.get(name) or default
