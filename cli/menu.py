from rich.prompt import Prompt
from core.engine import AegisEngine
from cli.banner import show_banner
from core.logger import log
import sys

def interactive_menu():
    show_banner()
    engine = AegisEngine()
    
    while True:
        log.info("\n[1] Recon & Analyze (Full Scan)\n[2] Doctor (Health Check)\n[3] Sair")
        choice = Prompt.ask("Selecione uma opção", choices=["1", "2", "3"])
        
        if choice == "1":
            target = Prompt.ask("Digite a URL alvo (ex: example.com)")
            engine.run_scan(target)
        elif choice == "2":
            from cli.commands import run_doctor
            run_doctor()
        elif choice == "3":
            log.info("Encerrando Aegis Scout...")
            sys.exit(0)
