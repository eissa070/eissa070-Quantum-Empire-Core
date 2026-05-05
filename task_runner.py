import os
import requests
import json

# 1. إعدادات الأمان والروابط
# بيسحب الرابط من السحابة، ولو ملقاش حاجة بيستخدم جوجل كاختبار بدل ما ينهار
target_url = os.getenv('TARGET_URL')
if not target_url or target_url == "None" or target_url.strip() == "":
    target_url = "https://www.google.com"

webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

# 2. قائمة البروكسيات (Elite Proxies) للتمويه
ELITE_PROXIES = [
    "161.35.70.249:8080",
    "138.197.148.215:8080",
    "167.71.230.134:8080"
]

def send_discord_log(message):
    if webhook_url:
        try:
            requests.post(webhook_url, json={"content": f"🛡️ **Eissa Empire Log:** {message}"})
        except:
            print("❌ Failed to send to Discord")

def run_mission():
    print(f"📡 Starting Radar on: {target_url}")
    
    # محاولة الاتصال بالموقع
    success = False
    for proxy in ELITE_PROXIES:
        try:
            # استخدام بروكسي للتمويه
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            res = requests.get(target_url, proxies=proxies, timeout=10)
            
            if res.status_code == 200:
                msg = f"✅ Target {target_url} is reachable via proxy {proxy}"
                print(msg)
                send_discord_log(msg)
                success = True
                break
        except Exception as e:
            print(f"⚠️ Proxy {proxy} failed, trying next...")

    if not success:
        # محاولة أخيرة بدون بروكسي لو الكل فشل
        try:
            res = requests.get(target_url, timeout=10)
            if res.status_code == 200:
                send_discord_log(f"⚠️ Reached {target_url} but WITHOUT proxy (Danger of Detection!)")
            else:
                send_discord_log(f"❌ Site {target_url} returned error {res.status_code}")
        except Exception as e:
            send_discord_log(f"🚨 Total Failure: Cannot reach {target_url}. Error: {str(e)}")

if __name__ == "__main__":
    run_mission()