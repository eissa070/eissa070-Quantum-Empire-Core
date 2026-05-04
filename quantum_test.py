import requests
import json
import time
from datetime import datetime

# إحداثيات بوابة ديسكورد الخاصة بك
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1500926382669041735/bkYZehWKKR8uEbm2pZ_ycz473vhAQgM9nta-_EituB7OPvQDiOiotBGKiP50vXeCshIW"

def send_to_discord(results, last_update):
    """إرسال تقرير حالة النظام إلى ديسكورد"""
    embed_fields = []
    status_summary = "✅ جميع الأنظمة مستقرة"
    
    for item in results:
        status_icon = "🟢" if "✅" in item['status'] else "🔴"
        if "❌" in item['status']:
            status_summary = "⚠️ تنبيه: تم رصد سقوط في الأنظمة!"
            
        embed_fields.append({
            "name": f"{status_icon} {item['name']}",
            "value": f"**الحالة:** {item['status']}\n**الاستجابة:** {item['latency']}\n**النوع:** {item['type']}",
            "inline": True
        })

    payload = {
        "username": "Quantum Empire Bot",
        "avatar_url": "https://i.imgur.com/4S2I2lM.png", # أيقونة افتراضية للرادار
        "embeds": [{
            "title": "📡 تقرير الرادار الإمبراطوري",
            "description": status_summary,
            "color": 65281 if "✅" in status_summary else 16711680, # أخضر أو أحمر
            "fields": embed_fields,
            "footer": {"text": f"آخر تحديث: {last_update}"}
        }]
    }

    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"فشل إرسال التقرير لديسكورد: {e}")

def check_targets():
    # الأهداف التي يراقبها الرادار حالياً
    targets = [
        {"name": "GitHub", "url": "https://github.com", "type": "DevOps Center"},
        {"name": "Google", "url": "https://www.google.com", "type": "Search Engine"}
    ]
    
    results = []
    last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for target in targets:
        try:
            start_time = time.time()
            response = requests.get(target['url'], timeout=10)
            latency = round(time.time() - start_time, 2)
            
            results.append({
                "name": target['name'],
                "type": target['type'],
                "status": "✅ Online",
                "latency": f"{latency}s"
            })
        except:
            results.append({
                "name": target['name'],
                "type": target['type'],
                "status": "❌ Offline",
                "latency": "N/A"
            })

    # 1. تحديث ملف JSON للموقع
    report = {"last_update": last_update, "data": results}
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    # 2. إرسال التقرير فوراً إلى ديسكورد
    send_to_discord(results, last_update)
    
    print(f"[{last_update}] تم تحديث الرادار وإرسال التقرير لديسكورد.")

if __name__ == "__main__":
    check_targets()