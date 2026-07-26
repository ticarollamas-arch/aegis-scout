from typing import Dict, List, Any
import re

class CookieAnalyzer:
    def analyze(self, headers: Dict[str, str]) -> List[Dict[str, Any]]:
        findings = []
        set_cookie = headers.get("Set-Cookie", "")
        if not set_cookie:
            return findings

        for cookie_str in set_cookie.split(', '):
            match = re.match(r'^([^=]+)=([^;]+);?', cookie_str)
            if not match: continue
            name = match.group(1).strip()
            
            if "Secure" not in cookie_str:
                findings.append({"type": "COOKIE_NO_SECURE", "severity": "HIGH", "description": f"Cookie {name} sem Secure"})
            if "HttpOnly" not in cookie_str:
                findings.append({"type": "COOKIE_NO_HTTPONLY", "severity": "MEDIUM", "description": f"Cookie {name} sem HttpOnly"})
                
        return findings
