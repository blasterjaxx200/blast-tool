import random
import os
import subprocess

# Fonction pour générer une adresse IP aléatoire
def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Fonction pour vérifier si une adresse IP est valide (ping)
def check_ip(ip):
    try:
        # Utilisation de la commande ping (sous Windows: 'ping -n 1', sous Linux/Mac: 'ping -c 1')
        output = subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True)
        return "1 packets transmitted, 1 received" in output  # Vérification du succès du ping sous Linux/Mac
    except subprocess.CalledProcessError:
        return False

# Fonction principale pour générer et vérifier des adresses IP
def generate_and_check_ips():
    valid_ips = []
    
    with open('ip.txt', 'w') as f:
        while len(valid_ips) < 10:
            ip = generate_random_ip()
            print(f"Checking IP: {ip}")
            if check_ip(ip):
                print(f"Valid IP found: {ip}")
                valid_ips.append(ip)
                f.write(ip + "\n")
            else:
                print(f"Invalid IP: {ip}")

    print("10 valid IP addresses found and saved to ip.txt")
    os.system('python3 main.py')  # Retour à main.py une fois terminé

if __name__ == "__main__":
    generate_and_check_ips()
