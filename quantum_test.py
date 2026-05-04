import requests
import json
import time
from datetime import datetime

def check_targets():
    # الأهداف اللي الرادار هيراقبها
    targets = [
        {"name": "GitHub", "url": "https://github.com", "type": "System Target"},
        {"name": "Google", "url": "https://www.google.com", "type": "System Target"}
    ]
    
    results = []
    for target in targets:
        try:
            start_time = time.time()
            response = requests.get(target['url'], timeout=10)
            latency = round(time.time() - start_time, 2)
            
            results.append({
                "name": target['name'],
                "type": target['type'],
                "status": "✅ Online",
                "latency": f"{latency}s" # دي اللي هتشيل كلمة Calculating وتظهر الرقم
            })
        except Exception as e:
            results.append({
                "name": target['name'],
                "type": target['type'],
                "status": "❌ Offline",
                "latency": "N/A"
            })

    # هيكل البيانات اللي الـ index.html مستنيه
    report = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": results
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    print("تم تحديث الرادار بنجاح!")

if __name__ == "__main__":
    check_targets()