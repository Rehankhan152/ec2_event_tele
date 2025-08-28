import os
import json
import requests

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))
    
    detail = event.get("detail", {})
    instance_id = detail.get("instance-id", "Unknown")
    state = detail.get("state", "Unknown")
    
    message = f"EC2 Instance *{instance_id}* changed state to *{state}*."
    send_telegram_message(message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent!')
    }