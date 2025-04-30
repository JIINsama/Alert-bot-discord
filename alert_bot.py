import os
import time
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

def send_alert():
    message = {
        "content": "🚨 테스트 알람 - Render 자동 실행 확인!"
    }
    response = requests.post(WEBHOOK_URL, json=message)
    if response.status_code == 204:
        print("✅ 알림 전송 성공")
    else:
        print(f"❌ 실패: {response.status_code}", response.text)

if __name__ == "__main__":
    while True:
        send_alert()
        time.sleep(3600)  # 1시간마다 전송 (실전에서는 5분, 6시간 등으로 조정)
