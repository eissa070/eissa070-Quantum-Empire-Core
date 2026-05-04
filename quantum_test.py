import requests
import json
import time
from datetime import datetime

def check_targets():
    # الأهداف التي يراقبها الرادار
    targets = [
        {"name": "GitHub", "url": "https://github.com", "type": "DevOps Center"},
        {"name": "Google", "url": "https://www.google.com", "type": "Search Engine"}
    ]
    
    results = []
    for target in targets:
        try:
            start_time = time.time()
            response = requests.get(target['url'], timeout=10)
            # حساب وقت الاستجابة بالثواني
            latency = round(time.time() - start_time, 2)
            
            results.append({
                "name": target['name'],
                "type": target['type'],
                "status": "✅ Online",
                "latency": f"{latency}s"  # كتابة الرقم بوضوح
            })
        except Exception as e:
            results.append({
                "name": target['name'],
                "type": target['type'],
                "status": "❌ Offline",
                "latency": "N/A"
            })

    # بناء الهيكل النهائي
    report = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": results
    }

    # حفظ الملف بصيغة UTF-8 لضمان ظهور الرموز
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    print("تم تحديث بيانات الإمبراطورية بنجاح!")

if __name__ == "__main__":
    check_targets()