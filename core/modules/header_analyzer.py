import re
from typing import Dict, List, Any

class HeaderAnalyzer:
    SECURITY_HEADERS = {
        "Strict-Transport-Security": {"required": True, "severity": "HIGH", "desc": "HSTS ausente"},
        "Content-Security-Policy": {"required": True, "severity": "HIGH", "desc": "CSP ausente"},
        "X-Content-Type-Options": {"required": True, "severity": "MEDIUM", "desc": "X-Content-Type-Options ausente"},
        "X-Frame-Options": {"required": True, "severity": "MEDIUM", "desc": "X-Frame-Options ausente"}
    }

    def analyze(self, headers: Dict[str, str]) -> List[Dict[str, Any]]:
        findings = []
        headers_lower = {k.lower(): v for k, v in headers.items()}
        
        for header, info in self.SECURITY_HEADERS.items():
            h_lower = header.lower()
            if h_lower not in headers_lower:
                if info["required"]:
                    findings.append({
                        "type": "MISSING_HEADER",
                        "header": header,
                        "severity": info["severity"],
                        "description": info["desc"]
                    })
            else:
                val = headers_lower[h_lower]
                if h_lower == "x-frame-options" and val.upper() not in ["DENY", "SAMEORIGIN"]:
                    findings.append({
                        "type": "WEAK_HEADER",
                        "header": header,
                        "severity": "MEDIUM",
                        "description": "X-Frame-Options fraco"
                    })
        return findings
