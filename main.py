# main.py
import os
import time

# Warna
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[97m'
B = '\033[94m'
END = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    print(f"""{C}
   ▄████  ▄▄▄       ██▀███   ▒█████   █    ██   ▄████  ▒█████  
  ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒ ██▒ ▀█▒▒██▒  ██▒
 ▒██░▄▄▄░▒██  ▀█▄  ▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▒██░▄▄▄░▒██░  ██▒
 ░▓█  ██▓░██▄▄▄▄██ ▒██▀▀█▄  ▒██   ██░▓▓█  ░██░░▓█  ██▓▒██   ██░
 ░▒▓███▀▒ ▓█   ▓██▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ░▒▓███▀▒░ ████▓▒░
  ░▒   ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒  ░▒   ▒ ░ ▒░▒░▒░ 
   ░   ░   ▒   ▒▒ ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░   ░   ░   ░ ▒ ▒░ 
 ░ ░   ░   ░   ▒     ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░ ░ ░   ░ ░ ░ ░ ▒  
       ░       ░  ░   ░         ░ ░     ░           ░     ░ ░  
{W}""")

def menu():
    print(f"{Y}[01] {W}Cek IP Publik")
    print(f"{Y}[02] {W}Spam OTP WhatsApp")
    print(f"{Y}[03] {W}Ngoding Python")
    print(f"{Y}[00] {W}Keluar")

def main():
    while True:
        banner()
        menu()
        choice = input(f"\n{G}Pilih menu > {W}")
        if choice == '1' or choice == '01':
            os.system('curl ifconfig.me')
            input(f"\n{C}Enter untuk kembali...")
        elif choice == '2' or choice == '02':
            print(f"{R}Fitur belum tersedia!{END}")
            time.sleep(1.5)
        elif choice == '3' or choice == '03':
            os.system('clear && python')
        elif choice == '0' or choice == '00':
            print(f"{G}Terima kasih!{END}")
            break
        else:
            print(f"{R}Pilihan tidak valid!{END}")
            time.sleep(1)

if __name__ == '__main__':
    main()
