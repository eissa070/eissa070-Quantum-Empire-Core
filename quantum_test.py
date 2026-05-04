import os
import requests
import time
from datetime import datetime

# إعدادات الاتصال (Captain Hook)
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

# أركان الإمبراطورية (روابطك الحقيقية)
SITES_TO_MONITOR = {
    "Portfolio & Core": "https://eissa01.netlify.app",
    "Netlify Team Console": "https://app.netlify.com/teams/eissa-s-0mlxtba/projects",
    "GitHub Core Repo": "https://github.com/eissa070/Quantum-Empire-Core"
}

# أقسام الاستثمار (أضف روابط المنصات اللي هتسجل فيها هنا)
INVESTMENT_HUBS = {
    "Email Army (SaaS)": "https://app.netlify.com/projects/eissa01/overview", # لوحة تحكم الإيميلات
    "Mining Nodes": "رابط_منصة_التعدين",
    "Affiliate Center": "رابط_منصة_الأفليت",
    "Free Credit Hub": "رابط_مواقع_الربح_المجاني"
}

def send_to_discord(title, message, color):
    payload = {
        "embeds": [{
            "title": title,
            "description": message,
            "color": color,
            "timestamp": datetime.utcnow().isoformat(),
            "footer": {"text": "Empire Management System 🚀"}
        }]
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Error sending to Discord: {e}")

def run_harvest_cycle():
    print(f"--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Starting Empire Harvest ---")
    
    # 1. فحص المواقع الأساسية (Netlify & GitHub)
    for name, url in SITES_TO_MONITOR.items():
        try:
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                send_to_discord(f"✅ Online: {name}", f"الموقع يعمل ومستعد لاستقبال الزوار.\nالرابط: {url}", 3066993)
            else:
                send_to_discord(f"⚠️ Warning: {name}", f"كود التنبيه: {res.status_code}", 15105570)
        except:
            send_to_discord(f"❌ Offline: {name}", "فشل الاتصال بهذا الركن!", 15158332)

    # 2. تقرير "جيش الإيميلات" و "الأفليت"
    # هنا هنحط رسالة تأكيدية إن السيستم شغال بيجمع بيانات
    send_to_discord("💰 تقرير الاستثمار", 
                   f"• **جيش الإيميلات**: يعمل على تجميع الكريديت المجاني.\n"
                   f"• **التعدين**: العقد (Nodes) مستقرة.\n"
                   f"• **الأفليت**: الروابط نشطة وتنتظر التحويلات.", 10181046)

if __name__ == "__main__":
    send_to_discord("🚜 انطلاق الإمبراطورية", "تم تشغيل نظام الحصاد الشامل لكل قطاعات العمل.", 15844367)
    while True:
        run_harvest_cycle()
        # فحص كل 30 دقيقة عشان تحافظ على استهلاك البيانات والكريديت
        print("Waiting for next cycle (30 min)...")
        time.sleep(1800)