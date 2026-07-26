from core.logger import log
from core.modules.scanner import WebScanner
from core.modules.header_analyzer import HeaderAnalyzer
from core.modules.ssl_checker import SSLChecker
from core.modules.cookie_analyzer import CookieAnalyzer
from core.modules.cors_tester import CORSTester
from reports.bug_report import BugReportGenerator
from datetime import datetime

class AegisEngine:
    def __init__(self):
        self.header_analyzer = HeaderAnalyzer()
        self.ssl_checker = SSLChecker()
        self.cookie_analyzer = CookieAnalyzer()
        self.cors_tester = CORSTester()
        self.reporter = BugReportGenerator()

    def run_scan(self, target: str):
        log.info(f"Iniciando auditoria em: {target}")
        if not target.startswith(('http://', 'https://')):
            target = f"https://{target}"

        scanner = WebScanner(target)
        response = scanner.fetch_page()
        
        if not response:
            log.error("Abortando scan devido a falha na requisição inicial.")
            return

        findings = []
        
        log.info("Analisando Headers...")
        h_findings = self.header_analyzer.analyze(response.headers)
        findings.extend(h_findings)
        if h_findings: log.warning(f"{len(h_findings)} problemas de header encontrados.")
        else: log.success("Headers OK.")

        log.info("Analisando SSL/TLS...")
        ssl_res = self.ssl_checker.check(target)
        findings.extend(ssl_res.get("findings", []))
        if ssl_res.get("findings"): log.warning("Problemas SSL encontrados.")
        else: log.success("SSL OK.")

        log.info("Analisando Cookies...")
        c_findings = self.cookie_analyzer.analyze(response.headers)
        findings.extend(c_findings)
        if c_findings: log.warning(f"{len(c_findings)} problemas de cookie encontrados.")
        else: log.success("Cookies OK.")

        log.info("Testando CORS...")
        cors_findings = self.cors_tester.test(target)
        findings.extend(cors_findings)
        if cors_findings: log.warning("Misconfiguração CORS detectada.")
        else: log.success("CORS OK.")

        score = self._calculate_score(findings)
        log.info(f"Score de Segurança Calculado: {score}/100")

        report_data = {
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "score": score,
            "findings": findings
        }
        
        report_path = self.reporter.generate(report_data)
        log.success(f"Relatório gerado em: {report_path}")

    def _calculate_score(self, findings: list) -> int:
        penalties = {"CRITICAL": 25, "HIGH": 15, "MEDIUM": 10, "LOW": 5}
        total_penalty = sum(penalties.get(f.get("severity", "LOW"), 5) for f in findings)
        return max(0, min(100, 100 - total_penalty))
