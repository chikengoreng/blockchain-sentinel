import requests
import time

API_URL = "https://api.blockchair.com/bitcoin/stats"

def fetch_blockchain_data():
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()["data"]
            print("⛓ Blockchain Sentinel Report:")
            print(f"  📦 Последний блок: {data['blocks']}")
            print(f"  🔄 Транзакций за 24ч: {data['transactions_24h']}")
            print(f"  💰 Объем за 24ч: {data['volume_24h_usd']} USD\n")
        else:
            print("⚠ Ошибка API:", response.status_code)
    except Exception as e:
        print("❌ Ошибка при запросе:", e)

if __name__ == "__main__":
    print("🚀 Blockchain Sentinel запущен. Обновление каждые 60 секунд.\n")
    while True:
        fetch_blockchain_data()
        time.sleep(60)
