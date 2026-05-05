import os
import requests
import random
import json

# --- إعدادات الهوية ---
DISCORD_WEBHOOK = os.getenv('DISCORD_WEBHOOK_URL')
FAIL_LOG_FILE = "fail_counts.json"
BLACKLIST_FILE = "blacklist.txt"

# --- إعدادات الحساسية والتمويه ---
MAX_RETRIES = 3 # يحظر الموقع بعد 3 محاولات فاشلة
ELITE_PROXIES = [
    "167.71.230.124:8080", "159.203.184.234:3128", 
    "138.68.60.8:8080", "161.35.70.249:3128"
]

def send_to_discord(title, msg, color=0x00ff41):
    if not DISCORD_WEBHOOK: return
    payload = {"embeds": [{"title": title, "description": msg, "color": color}]}
    requests.post(DISCORD_WEBHOOK, json=payload)

def load_data(file, default):
    if not os.path.exists(file): return default
    with open(file, "r") as f: 
        try: return json.load(f) if file.endswith('.json') else f.read().splitlines()
        except: return default

def save_blacklist(domain):
    with open(BLACKLIST_FILE, "a") as f: f.write(domain + "\n")
    send_to_discord("🚫 حظر تلقائي", f"تم نفي النطاق {domain} إلى القائمة السوداء بعد {MAX_RETRIES} محاولات فاشلة.", 0xff0000)

def run_mission(target_url):
    if not target_url: return
    domain = target_url.split("//")[-1].split("/")[0]
    
    # فحص الحظر
    if domain in load_data(BLACKLIST_FILE, []):
        print(f"⏭️ {domain} محظور.")
        return

    fail_data = load_data(FAIL_LOG_FILE, {})
    proxy = random.choice(ELITE_PROXIES)
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}
        res = requests.get(target_url, proxies={"http": f"http://{proxy}"}, headers=headers, timeout=10)
        
        if res.status_code == 200:
            send_to_discord("✅ نجاح العملية", f"الموقع: {domain}\nالتمويه: {proxy}")
            fail_data[domain] = 0
            # هنا يشتغل رادار العطور تلقائياً
            if "perfume" in target_url or "fragrance" in target_url:
                send_to_discord("📡 رادار العطور", f"تم فحص أهداف جديدة في {domain}")
        else:
            raise Exception("Failed")
    except:
        count = fail_data.get(domain, 0) + 1
        fail_data[domain] = count
        if count >= MAX_RETRIES:
            save_blacklist(domain)
            fail_data[domain] = 0
    
    with open(FAIL_LOG_FILE, "w") as f: json.dump(fail_data, f)

if __name__ == "__main__":
    run_mission(os.getenv('TARGET_URL'))