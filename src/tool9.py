import os
import subprocess
from datetime import datetime

# Crée le dossier 'scan' s'il n'existe pas
if not os.path.exists('scan'):
    os.makedirs('scan')

# Nom du fichier avec la date et l'heure
filename = os.path.join('scan', f'scan_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')

def run_clamscan(directory):
    try:
        result = subprocess.run(['clamscan', '--recursive', '--log=' + filename, directory], capture_output=True, text=True)
        if result.returncode == 0:
            return "Analyse terminée sans détection de virus."
        else:
            return "Des virus ou logiciels malveillants ont été détectés. Consultez le fichier de log pour plus de détails."
    except FileNotFoundError:
        return "ClamAV n'est pas installé ou non trouvé."

# Chemin du répertoire à analyser
directory_to_scan = '/'

# Effectuer l'analyse
scan_result = run_clamscan(directory_to_scan)

# Écrire le résultat dans le fichier
with open(filename, 'w') as file:
    file.write(f"Date et Heure de l'analyse: {datetime.now()}\n")
    file.write(scan_result)
    file.write("\n\nDétails de l'analyse:\n")
    with open(filename, 'r') as log_file:
        file.write(log_file.read())

print(f"L'analyse a été enregistrée dans '{filename}'. Cliquez sur l'espace pour revenir à main.")
