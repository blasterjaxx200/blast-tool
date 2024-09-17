import os
import psutil
import platform
import distro
from datetime import datetime

# Crée le dossier 'scan' s'il n'existe pas
if not os.path.exists('scan'):
    os.makedirs('scan')

# Nom du fichier avec la date et l'heure
filename = os.path.join('scan', f'system_info_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')

def get_system_info():
    info = []
    info.append(f"Date et Heure: {datetime.now()}")
    info.append(f"Système: {platform.system()}")
    info.append(f"Nom du système: {platform.node()}")
    info.append(f"Version du système: {platform.version()}")
    info.append(f"Distribution: {distro.name()} {distro.version()}")
    info.append(f"Machine: {platform.machine()}")
    info.append(f"Architecture: {platform.architecture()}")
    info.append(f"Processeur: {platform.processor()}")
    
    info.append("\nInformations sur le CPU:")
    info.append(f"Nombre de coeurs: {psutil.cpu_count(logical=True)}")
    info.append(f"Fréquence du CPU: {psutil.cpu_freq().max} MHz")

    info.append("\nInformations sur la mémoire:")
    mem = psutil.virtual_memory()
    info.append(f"Mémoire totale: {mem.total / (1024 ** 3):.2f} Go")
    info.append(f"Mémoire disponible: {mem.available / (1024 ** 3):.2f} Go")
    info.append(f"Utilisation: {mem.percent}%")

    info.append("\nInformations sur le stockage:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        info.append(f"Partition: {partition.device}")
        usage = psutil.disk_usage(partition.mountpoint)
        info.append(f"  Total: {usage.total / (1024 ** 3):.2f} Go")
        info.append(f"  Utilisé: {usage.used / (1024 ** 3):.2f} Go")
        info.append(f"  Libre: {usage.free / (1024 ** 3):.2f} Go")
        info.append(f"  Pourcentage utilisé: {usage.percent}%")
    
    return "\n".join(info)

# Écrit les informations dans le fichier
with open(filename, 'w') as file:
    file.write(get_system_info())

print(f"Les informations système ont été enregistrées dans '{filename}'")
