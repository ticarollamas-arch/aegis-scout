from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_banner():
    banner_text = """
╔══════════════════════════════════╗
║         AEGIS FRAMEWORK          ║
║     Enterprise CLI Platform      ║
║          [ SCOUT ]               ║
╚══════════════════════════════════╝
    """
    text = Text(banner_text, style="bold cyan", justify="center")
    text.append("\nVersion: 1.0.0 | Status: Ready", style="bold green")
    console.print(text)
