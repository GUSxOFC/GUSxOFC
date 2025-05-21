# main.py
import os
import requests
import time

# Warna
R = '\033[91m'; G = '\033[92m'; Y = '\033[93m'; B = '\033[94m'; C = '\033[96m'; W = '\033[97m'; END = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    print(f"""{C}
  ▄████  ▄▄▄       ██▀███   ▒█████   █    ██ 
 ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░
░▓█  ██▓░██▄▄▄▄██ ▒██▀▀█▄  ▒██   ██░▓▓█  ░██░
░▒▓███▀▒ ▓█   ▓██▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ 
 ░▒   ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ 
  ░   ░   ▒   ▒▒ ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ 
░ ░   ░   ░   ▒     ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░ 
      ░       ░  ░   ░         ░ ░     ░     
  ░ TOOLS BY GusOfc1
{W}""")

def menu():
    print(f"{Y}[1] {W}Cek Info IP Target")
    print(f"{Y}[2] {W}Cek Info IP Anda")
    print(f"{Y}[3] {W}Tampilkan Lokasi IP (dengan Map Link)")
    print(f"{Y}[0] {W}Keluar")

def ip_lookup(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res['status'] == 'success':
            print(f"{G}IP: {res['query']}")
            print(f"{G}Negara: {res['country']}")
            print(f"{G}Kota: {res['city']}")
            print(f"{G}Provider: {res['isp']}")
            print(f"{G}Koordinat: {res['lat']}, {res['lon']}")
            print(f"{Y}Google Maps: https://maps.google.com/?q={res['lat']},{res['lon']}")
        else:
            print(f"{R}IP tidak ditemukan!")
    except Exception as e:
        print(f"{R}Gagal mengambil data! Error: {e}")

def main():
    while True:
        banner()
        menu()
        choice = input(f"\n{C}Pilih menu > {W}")
        if choice == '1':
            ip = input(f"{Y}Masukkan IP target: {W}")
            ip_lookup(ip)
            input(f"\n{C}Enter untuk kembali...")
        elif choice == '2':
            ip = requests.get("https://ifconfig.me").text
            print(f"{G}IP Kamu: {ip}")
            input(f"\n{C}Enter untuk kembali...")
        elif choice == '3':
            ip = input(f"{Y}Masukkan IP target: {W}")
            res = requests.get(f"http://ip-api.com/json/{ip}").json()
            if res['status'] == 'success':
                print(f"{G}Maps: https://maps.google.com/?q={res['lat']},{res['lon']}")
            else:
                print(f"{R}Tidak ditemukan!")
            input(f"\n{C}Enter untuk kembali...")
        elif choice == '0':
            print(f"{G}Keluar...{END}")
            break
        else:
            print(f"{R}Pilihan tidak valid!{END}")
            time.sleep(1.5)

if __name__ == '__main__':
    main()
            
