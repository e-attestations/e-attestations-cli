#!/usr/bin/env python3
'''The colored version of e-Attestations' banner'''
from colorama import init, Fore, Style

def colored():
    '''Displays the colored banner'''
    # Initialize colorama
    init(autoreset=True)
    print(Fore.CYAN + "╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print(Fore.CYAN + "║                                                                                         "+Fore.GREEN+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+ Fore.CYAN +"      ║")
    print(Fore.CYAN + "║  "+ Fore.GREEN +"e-Attestations.com - Third-Party Management Solutions & Services                       "+Fore.GREEN+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+Fore.CYAN +"       ║")
    print(Fore.CYAN + "║  All right reserved/Tous droits réservés                                                "+Fore.GREEN+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+ Fore.CYAN +"        ║")
    print(Fore.CYAN + "║                  _   _            _        _   _                                        "+Fore.GREEN+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓,     ▓"+ Fore.CYAN +"  ║")
    print(Fore.CYAN + "║             /\  | | | |          | |      | | (@)                                       "+Fore.GREEN+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓.     ▓▓"+ Fore.CYAN +"  ║")
    print(Fore.CYAN + "║  ___       /  \ | |_| |_ ___  ___| |_ __ _| |_ _  ___  _ __  ___   ___ ___  _ __ ___    "+Fore.GREEN+"▓▓▓▓▓▓▓▓▓▓▓▓▓,      ▓▓▓"+ Fore.CYAN +"  ║")
    print(Fore.CYAN + "║ / _ \  __ / /\ \| __| __/ _ \/ __| __/ _` | __| |/ _ \| '_ \/ __| / __/ _ \| '_ ` _ \   "+Fore.GREEN+"▓▓▓▓▓▓▓▓▓▓▓▓,     .▓▓▓▓"+ Fore.CYAN +"  ║")
    print(Fore.CYAN + "║|  __//__ / ____ \ |_| ||  __/\__ \ || (_| | |_| | (_) | | | \__ \| (_| (_) | | | | | |  "+Fore.GREEN+" .▓▓▓▓▓▓▓▓▓.     ,▓▓▓▓▓"+ Fore.CYAN +"  ║")
    print(Fore.CYAN + "║ \___/   /_/    \_\__|\__\___||___/\__\__,_|\__|_|\___/|_| |_|___(_)___\___/|_| |_| |_|  "+Fore.GREEN+"    .▓▓▓▓▓      ,▓▓▓▓▓▓"+ Fore.CYAN +"  ║")
    print(Fore.CYAN + "║                                                                                         "+Fore.GREEN+"       .,      .▓▓▓▓▓▓▓"+ Fore.CYAN +"  ║")
    print(Fore.CYAN + "║                                                                                         "+Fore.GREEN+"▓,           ,▓▓▓▓▓▓▓▓▓"+ Fore.CYAN +"  ║")
    print(Fore.CYAN + "╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print(Fore.GREEN + ":: e-Attestations.com (https://www.e-attestations.com) :: "+ Fore.GREEN +"\ö/ "+ Fore.YELLOW +"★★★★ 😎")

if __name__ == '__main__':
    colored()