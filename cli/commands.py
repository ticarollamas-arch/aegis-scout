import typer
import sys
from core.engine import AegisEngine
from core.logger import log
from cli.banner import show_banner
from cli.menu import interactive_menu

app = typer.Typer(help="Aegis Scout - Enterprise Web Auditor")

@app.command()
def scan(target: str = typer.Option(..., "--target", "-t", help="URL alvo para auditoria")):
    """Executa auditoria passiva em um alvo específico."""
    show_banner()
    engine = AegisEngine()
    engine.run_scan(target)

@app.command()
def doctor():
    """Verifica a saúde do sistema e dependências."""
    show_banner()
    run_doctor()

@app.command()
def interactive():
    """Inicia o menu interativo."""
    interactive_menu()

def run_doctor():
    log.info("Iniciando diagnóstico do sistema...")
    
    # Check Python
    py_version = sys.version_info
    if py_version.major >= 3 and py_version.minor >= 11:
        log.success(f"Python Version: {py_version.major}.{py_version.minor} (OK)")
    else:
        log.warning(f"Python Version: {py_version.major}.{py_version.minor} (Recomendado 3.11+)")

    # Check Dependencies
    try:
        import requests
        log.success(f"Requests module loaded (v{requests.__version__})")
    except ImportError:
        log.error("Requests module missing. Run: pip install requests")

    try:
        import rich
        log.success(f"Rich module loaded (v{rich.__version__})")
    except ImportError:
        log.error("Rich module missing. Run: pip install rich")
        
    log.info("Diagnóstico concluído.")
