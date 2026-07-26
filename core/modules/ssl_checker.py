import ssl
import socket
import datetime
from typing import Dict, Any
from urllib.parse import urlparse
from core.logger import log

class SSLChecker:
    def check(self, url: str) -> Dict[str, Any]:
        parsed = urlparse(url)
        hostname = parsed.hostname or url
        port = parsed.port or 443
        
        result = {"valid": False, "protocol": "Unknown", "findings": []}
        
        if parsed.scheme != 'https':
            return result

        try:
            context = ssl.create_default_context()
            with socket.create_connection((hostname, port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    result["valid"] = True
                    result["protocol"] = ssock.version()
                    cert = ssock.getpeercert()
                    if cert:
                        expiry = datetime.datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
                        days = (expiry - datetime.datetime.now()).days
                        if days < 30:
                            result["findings"].append({
                                "type": "CERT_EXPIRING",
                                "severity": "HIGH",
                                "description": f"Expira em {days} dias"
                            })
        except Exception as e:
            log.warning(f"Erro ao verificar SSL: {str(e)}")
            result["findings"].append({"type": "SSL_ERROR", "severity": "HIGH", "description": str(e)})
        
        return result
