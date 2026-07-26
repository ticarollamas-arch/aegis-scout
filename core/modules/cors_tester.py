import requests
from typing import List, Dict, Any
from core.config import Config
from core.logger import log

class CORSTester:
    def test(self, target: str) -> List[Dict[str, Any]]:
        findings = []
        test_origin = "https://evil.com"
        headers = {"Origin": test_origin}
        
        try:
            res = requests.options(target, headers=headers, timeout=Config.TIMEOUT)
            acao = res.headers.get("Access-Control-Allow-Origin", "")
            acac = res.headers.get("Access-Control-Allow-Credentials", "")
            
            if acao == "*" or acao == test_origin:
                findings.append({
                    "type": "CORS_MISCONFIG",
                    "severity": "HIGH",
                    "description": f"CORS permite origem arbitrária: {acao}"
                })
                if acac.lower() == "true":
                    findings.append({
                        "type": "CORS_CREDENTIALS",
                        "severity": "CRITICAL",
                        "description": "CORS permite credenciais com origem arbitrária"
                    })
        except requests.exceptions.RequestException as e:
            log.warning(f"Falha ao testar CORS: {str(e)}")
            
        return findings
