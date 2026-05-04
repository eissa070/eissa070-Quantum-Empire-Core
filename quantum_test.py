import requests
import json
from datetime import datetime

# قائمة المواقع التي تريد مراقبتها
targets = [
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "GitHub", "url": "https://github.com"},
    # أضف روابطك الخاصة هنا
]

def check_empire():
    results = []
    print(f"[{datetime.now()}] Starting Empire Radar scan...")
    
    for target in targets:
        try:
            # timeout=10 يمنع الكود من التعليق لو الموقع لم يرد
            response = requests.get(target["url"], timeout=10)
            status = "Online ✅" if response.status_code == 200 else f"Issue ⚠️ ({response.status_code})"
        except Exception as e:
            status = "Offline ❌"
        
        results.append({
            "name": target["name"],
            "url": target["url"],
            "status": status,
            "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Checked {target['name']}: {status}")

    # حفظ النتائج في ملف data.json ليقرأه الموقع
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    print("Mission accomplished. Data saved to data.json")

if __name__ == "__main__":
    check_empire()