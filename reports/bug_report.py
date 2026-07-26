import os
import json
from datetime import datetime
from core.config import Config

class BugReportGenerator:
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)

    def generate(self, data: dict) -> str:
        target_clean = data['target'].replace('https://', '').replace('http://', '').replace('/', '_')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"aegis_report_{target_clean}_{timestamp}.json"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        return filepath
