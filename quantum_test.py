import requests
import json
from datetime import datetime

# الأهداف المتطورة (يمكنك إضافة روابط الـ API أو المواقع هنا)
targets = [
    {"name": "Google", "url": "https://www.google.com", "type": "Search"},
    {"name": "GitHub", "url": "https://github.com", "type": "DevOps"},
    # أضف مواقع الاستثمار أو التعدين الخاصة بك هنا
]

def harvest_intelligence():
    results = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "empire_status": "Active ⚡",
        "data": []
    }
    
    print(f"--- [Starting Intelligence Session: {results['last_update']}] ---")
    
    for target in targets:
        try:
            # إضافة headers لمحاكاة متصفح حقيقي لتجنب الحظر
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            start_time = datetime.now()
            response = requests.get(target["url"], timeout=15, headers=headers)
            end_time = datetime.now()
            
            # حساب سرعة الاستجابة بالثواني
            latency = (end_time - start_time).total_seconds()
            
            status = "Online ✅" if response.status_code == 200 else f"Slow/Issue ({response.status_code})"
            
            results["data"].append({
                "name": target["name"],
                "type": target["type"],
                "status": status,
                "latency": f"{latency:.2f}s",
                "health_score": 100 if latency < 1 else 50
            })
            print(f"Successfully harvested: {target['name']} | Latency: {latency:.2f}s")
            
        except Exception as e:
            results["data"].append({
                "name": target["name"],
                "type": target["type"],
                "status": "Target Down ❌",
                "error": str(e)[:50]
            })
            print(f"Critical Failure at: {target['name']}")

    # حفظ البيانات في ملف data.json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    print(f"--- [Session Closed. Intelligence Stored in data.json] ---")

if __name__ == "__main__":
    harvest_intelligence()