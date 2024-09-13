import os
import fade
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
                   ╔═════════════════════════════╗
                   ║                             ║
                   ║ [1] phone info              ║
                   ║                             ║
                   ║ [2] discord nitro generator ║
                   ║                             ║ 
                   ║ [3] phising attack          ║
                   ╚═════════════════════════════╝
                                  """  
menu = fade.fire(menu)

def main():
    os.system("clear")  # Remplace 'cls' par 'clear' pour Linux
    print(banner)  # Affiche bien le banner
    print()
    print(menu)
    choice = input("choice : ")
    if choice == "1":
        os.system("python tool1.py")
    if choice == "2":
        os.system("python tool2.py")
    if choice == "3":
        os.system("python tool3.py")
    else:
        print("merci de rentrer un nombre valide")
        main()

main()
