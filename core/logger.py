from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "red bold"
})

console = Console(theme=custom_theme)

class AegisLogger:
    @staticmethod
    def info(msg: str):
        console.print(f"[info][+][/info] {msg}")

    @staticmethod
    def success(msg: str):
        console.print(f"[success][✓][/success] {msg}")

    @staticmethod
    def warning(msg: str):
        console.print(f"[warning][!][/warning] {msg}")

    @staticmethod
    def error(msg: str):
        console.print(f"[error][-][/error] {msg}")

    @staticmethod
    def print_json(data: dict):
        console.print_json(data=data)

log = AegisLogger()
