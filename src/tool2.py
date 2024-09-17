import random
import string
import json
import requests
import threading
import os
import time

# Définir le nombre de threads
threads_number = 5

# Webhook (optionnel)
webhook = input("Webhook ? (y/n) -> ")
if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
    webhook_url = input("Webhook Url -> ")

# Fonction d'envoi au webhook
def send_webhook(url_nitro):
    payload = {
        'embeds': [{
            'title': 'Nitro Valid !',
            'description': f"**Nitro:**\n```{url_nitro}```",
            'color': 0x00FF00
        }],
        'username': 'Nitro Checker',
        'avatar_url': 'https://example.com/avatar.png'
    }

    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, data=json.dumps(payload), headers=headers)

# Fonction pour vérifier si un code Nitro est valide
def nitro_check():
    code_nitro = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(16)])
    url_nitro = f'https://discord.gift/{code_nitro}'
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)

    if response.status_code == 200:
        print(f"Valid Nitro: {url_nitro}")
        with open('nitro.txt', 'a') as f:
            f.write(f"{url_nitro}\n")
        
        if webhook in ['y']:
            send_webhook(url_nitro)
        
        print("Returning to main.py...")
        time.sleep(2)
        os.system('python3 main.py')  # Retourne à main.py après avoir trouvé un code valide
        return True
    else:
        print(f"Invalid Nitro: {url_nitro}")
        return False

# Fonction pour démarrer plusieurs threads
def request():
    threads = []
    try:
        for _ in range(int(threads_number)):
            t = threading.Thread(target=nitro_check)
            t.start()
            threads.append(t)
    except Exception as e:
        print(f"Erreur : {e}")

    for thread in threads:
        thread.join()

# Boucle principale
if __name__ == "__main__":
    while True:
        request()

