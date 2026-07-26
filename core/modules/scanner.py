import requests
import time
from typing import Optional, Dict
from urllib.parse import urlparse
from core.logger import log
from core.config import Config

class WebScanner:
    def __init__(self, target: str):
        self.target = target
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": Config.USER_AGENT,
            "Accept": "application/json, text/html, application/xml",
            "X-Research-Purpose": "true"
        })

    def fetch_page(self) -> Optional[requests.Response]:
        try:
            time.sleep(1.0 / Config.RATE_LIMIT)
            log.info(f"Iniciando requisição para {self.target} (Timeout: {Config.TIMEOUT}s)")
            response = self.session.get(
                self.target,
                timeout=Config.TIMEOUT,
                allow_redirects=True,
                verify=True
            )
            response.raise_for_status()
            log.success(f"Status: {response.status_code} | Tamanho: {len(response.content)} bytes")
            return response

        except requests.exceptions.Timeout:
            log.error(f"Timeout excedido ({Config.TIMEOUT}s) ao acessar {self.target}")
            return None
        except requests.exceptions.ConnectionError:
            log.error(f"Falha de conexão (Recusada/Queda) com {self.target}")
            return None
        except requests.exceptions.HTTPError as http_err:
            log.warning(f"Erro HTTP retornado pelo servidor: {http_err}")
            # Retorna a resposta mesmo com erro HTTP (ex: 403, 404) para analisar headers
            return http_err.response 
        except Exception as e:
            log.error(f"Erro inesperado durante a requisição: {str(e)}")
            return None
