import os
import requests
import json
from datetime import datetime

# إعدادات الاتصال من خزنة GitHub
DISCORD_WEBHOOK = os.getenv('DISCORD_WEBHOOK')

# أركان الإمبراطورية (روابطك الحقيقية اللي كانت في كودك القديم)
SITES_TO_MONITOR = {
    "Portfolio & Core": "https://eissa01.netlify.app",
    "Netlify Team Console": "https://app.netlify.com/teams/eissa-s-0mlxtba/projects",
    "GitHub Core Repo": "https://github.com/eissa070/Quantum-Empire-Core"
}

def harvest_data():
    print(f"--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Starting Empire Harvest ---")
    results = []
    
    # فحص المواقع وتجهيز بيانات الجدول
    for name, url in SITES_TO_MONITOR.items():
        try:
            res = requests.get(url, timeout=15)
            status = "Active ✅" if res.status_code == 200 else f"Error {res.status_code} ⚠️"
        except:
            status = "Offline ❌"
        
        results.append({
            "node_name": name,
            "status": status,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "size": "N/A" # أو أي قيمة تحب تعرضها
        })

    # 1. حفظ البيانات في ملف JSON للموقع
    with open('data.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("✅ Data archived to data.json")

    # 2. إرسال التقرير المجمع لديسكورد (بشكل احترافي)
    if DISCORD_WEBHOOK:
        report = "🚜 **تقرير حصاد الإمبراطورية الدوري**\n"
        for r in results:
            report += f"• {r['node_name']}: {r['status']}\n"
        
        requests.post(DISCORD_WEBHOOK, json={"content": report})
        print("✅ Report sent to Discord")

if __name__ == "__main__":
    harvest_data()