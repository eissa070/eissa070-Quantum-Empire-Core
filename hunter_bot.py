import requests

# إعدادات الإمبراطورية
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1500926382669041735/bkYZehWKKR8uEbm2pZ_ycz473vhAQgM9nta-_EituB7OPvQDiOiotBGKiP50vXeCshIW"

def hunt_for_money():
    # محاكاة البحث عن أرصدة المطورين (GitHub & Google Cloud)
    opportunities = [
        "تم اكتشاف رصيد 200$ مخصص لمطوري Python في Azure.",
        "تنبيه: Airdrop جديد لمشاريع الـ Testnet متاح الآن."
    ]
    
    for opt in opportunities:
        payload = {"content": f"💰 **فرصة تمويل جديدة:** {opt}"}
        requests.post(DISCORD_WEBHOOK, json=payload)
        print(f"تم إرسال التنبيه: {opt}")

if __name__ == "__main__":
    hunt_for_money()