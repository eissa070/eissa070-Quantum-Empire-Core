import os
import requests
import json

# حماية من الروابط الفارغة - لو مفيش رابط بيفحص جوجل كاختبار
target_url = os.getenv('TARGET_URL')
if not target_url or target_url == "None" or target_url.strip() == "":
    target_url = "https://www.google.com"

webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

# قائمة بروكسيات قوية للتمويه
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
            print("❌ Discord Webhook Error")

def run_mission():
    print(f"📡 Starting Radar on: {target_url}")
    success = False
    
    for proxy in ELITE_PROXIES:
        try:
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            res = requests.get(target_url, proxies=proxies, timeout=10)
            if res.status_code == 200:
                msg = f"✅ Target {target_url} reached via proxy {proxy}"
                send_discord_log(msg)
                success = True
                break
        except:
            continue

    if not success:
        try:
            res = requests.get(target_url, timeout=10)
            status = "Success" if res.status_code == 200 else f"Failed ({res.status_code})"
            send_discord_log(f"⚠️ Radar finished on {target_url} | Result: {status}")
        except Exception as e:
            send_discord_log(f"🚨 Radar Error: {str(e)}")

if __name__ == "__main__":
    run_mission()