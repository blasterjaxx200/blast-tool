import os
import fade
import time
from fade import *

banner = r"""
   ___   .__                   __                   __                .__   
\_ |__ |  | _____    _______/  |_  ___________  _/  |_  ____   ____ |  |  
 | __ \|  | \__  \  /  ___/\   __\/ __ \_  __ \ \   __\/  _ \ /  _ \|  |  
 | \_\ \  |__/ __ \_\___ \  |  | \  ___/|  | \/  |  | (  <_> |  <_> )  |__
 |___  /____(____  /____  > |__|  \___  >__|     |__|  \____/ \____/|____/
     \/          \/     \/            \/                                  
"""
banner = fade.fire(banner)

menu = """
                   ╔═══════════════════════════════════════════════════╗
                   ║                                                   ║
                   ║ [1] phone info                [6] dox ip          ║
                   ║                                                   ║
                   ║ [2] discord nitro generator   [7] ip gen          ║
                   ║                                                   ║ 
                   ║ [3] create file dox           [8] scan pc         ║ 
                   ║                                                   ║ 
                   ║ [4] darkweb link              [9] ip lookup       ║ 
                   ║                                                   ║ 
                   ║ [5] website scan              [10] token joiner   ║ 
                   ╚═══════════════════════════════════════════════════╝


                   ╔═══════════════════════════════════════════════════╗
                   ║                                                   ║
                   ║ [11] discord server info       [16] soon          ║
                   ║                                                   ║
                   ║ [12] execute Builder.bat       [17] soon          ║
                   ║                                                   ║ 
                   ║ [13] soon                      [18] soon          ║ 
                   ║                                                   ║ 
                   ║ [14] soon                      [19] soon          ║ 
                   ║                                                   ║ 
                   ║ [15] soon                      [20] soon          ║ 
                   ╚═══════════════════════════════════════════════════╝
"""
menu = fade.fire(menu)

def clear_screen():
    """Clear the console screen depending on the OS."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux
        os.system('clear')

def main():
    clear_screen()  # Nettoie l'écran
    print(banner)  # Affiche le banner en dégradé de feu
    print(menu)  # Affiche le menu

    choice = input("choice : ")

    if choice == "1":
        os.system("python src/tool1.py")
    elif choice == "2":
        os.system("python src/tool2.py")
    elif choice == "3":
        os.system("python src/tool3.py")
    elif choice == "4":
        os.system("python src/tool4.py")
    elif choice == "5":
        os.system("python src/tool5.py")
    elif choice == "6":
        os.system("python src/tool6.py")
    elif choice == "7":
        os.system("python src/tool7.py")
    elif choice == "8":
        os.system("python src/tool8.py")
    elif choice == "9":
        os.system("python src/tool9.py")
    elif choice == "10":
        os.system("python src/tool10.py")
    elif choice == "11":
        os.system("python src/tool11.py")
    elif choice == "12":
        # Utilisation du chemin complet ou relatif compatible Windows
        os.system(r'src\\Builder.bat')  # ou utilise le chemin complet
    else:
        print("Merci de rentrer un nombre valide.")
        time.sleep(1)  # Pause pour afficher l'erreur
        main()  # Réaffiche le menu

main()


