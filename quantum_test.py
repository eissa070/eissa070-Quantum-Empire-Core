import requests
import json
import time
from datetime import datetime

def check_targets():
    targets = [
        {"name": "Google", "url": "https://www.google.com", "type": "Search Engine"},
        {"name": "GitHub", "url": "https://github.com", "type": "Dev Ops"}
    ]
    
    results = []
    for target in targets:
        try:
            start_time = time.time()
            response = requests.get(target['url'], timeout=10)
            end_time = time.time()
            
            # حساب السرعة بدقة
            latency = round(end_time - start_time, 2)
            
            results.append({
                "name": target['name'],
                "url": target['url'],
                "type": target['type'],
                "status": "✅ Online",
                "latency": f"{latency}s"  # هنا السرعة بتتحسب وتتكتب
            })
        except:
            results.append({
                "name": target['name'],
                "status": "❌ Offline",
                "latency": "N/A"
            })

    # الهيكل الجديد اللي الـ HTML بيفهمه
    final_data = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": results
    }

    with open('data.json', 'w') as f:
        json.dump(final_data, f, indent=4)

if __name__ == "__main__":
    check_targets()