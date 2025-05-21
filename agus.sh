31m'in/bash

# Warna
red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
cyan='\033[1;36m'
purple='\033[1;35m'
bold='\033[1m'
nc='\033[0m'

clear

# Banner
echo -e "${purple}${bold}"
figlet "GusOfc" | lolcat

echo -e "${green}Welcome to bot GusOfc!${nc}"
echo -e "${yellow}Apa yang dapat kami bantu?${nc}\n"

# Login
read -p "Masukkan username: " user
read -s -p "Masukkan password: " pw

echo ""

if [[ $user != "GusOfc" || $pw != "123" ]]; then
  echo -e "${red}Login gagal. Username atau password salah.${nc}"
  exit 1
fi

clear
echo -e "${blue}${bold}Login berhasil! Selamat datang, $user.${nc}"
sleep 1

# IP Publik
ip=$(curl -s https://ipinfo.io/ip)
echo -e "${cyan}IP Publik kamu: ${green}$ip${nc}"
sleep 1

# Menu
while true; do
  echo -e "\n${purple}========== MENU BOT GUSOFC ==========${nc}"
  echo -e "${yellow}[1] Cek Khodam"
  echo "[2] Ramalan Kehidupan"
  echo "[3] Seberapa Akrab Kamu?"
  echo "[4] Spam Pesan WA (20x)"
  echo "[5] Cek IP (simulasi)"
  echo "[6] Cek South (simulasi)"
  echo "[7] Cek Asia (simulasi)"
  echo "[8] Cek Kartu (simulasi)"
  echo "[9] DOX (simulasi)"
  echo "[10] GusOfc (AI Chat)"
  echo "[11] Info Bot"
  echo "[0] Keluar${nc}"
  echo -e "${purple}=====================================${nc}"

  read -p "Pilih menu: " menu

  case $menu in
    1)
      read -p "Masukkan nama kamu: " nama
      echo -e "${green}Khodam kamu bernama 'Singo Barong', pelindung ghaib ${nama}.${nc}"
      ;;
    2)
      read -p "Nama kamu: " nama
      read -p "Tanggal Lahir (YYYY-MM-DD): " ttl
      echo -e "${cyan}Ramalan: Hidup $nama akan penuh warna setelah $ttl. Tetap semangat!${nc}"
      ;;
    3)
      read -p "Nama kamu: " kamu
      read -p "Nama pasangan: " doi
      persen=$((RANDOM % 100 + 1))
      echo -e "${blue}Kamu dan $doi akrab sebesar: ${green}$persen%${nc}"
      ;;
    4)
      read -p "Nomor WhatsApp (08xxxx): " wa
      echo -e "${red}Mengirim spam ke WA $wa${nc}"
      for i in {1..20}; do
        sender=$(shuf -n1 -e "Bank Indonesia" "BCA" "Dana Indonesia" "Shopay" "Gopay" "OVO" "Seabank" "Cerah Pedia")
        echo -e "${yellow}[SPAM $i] Pesan dari $sender ke $wa${nc}"
        sleep 0.2
      done
      ;;
    5)
      read -p "Masukkan nomor WA: " wa
      echo -e "${cyan}IP dari $wa: 123.456.78.$((RANDOM % 255)) (simulasi)${nc}"
      ;;
    6)
      read -p "Masukkan nomor WA: " wa
      echo -e "${cyan}South Trace: Jakarta Selatan, lokasi terakhir: Blok M (simulasi)${nc}"
      ;;
    7)
      read -p "Masukkan nomor WA: " wa
      echo -e "${cyan}Asia Trace: Terhubung dari server Singapura (simulasi)${nc}"
      ;;
    8)
      read -p "Masukkan nomor WA: " wa
      echo -e "${cyan}Kartu aktif sejak 2021-04-01, akan habis masa aktif: 2025-12-31 (simulasi)${nc}"
      ;;
    9)
      read -p "Masukkan NIK: " nik
      echo -e "${red}Data dari NIK $nik:${nc}"
      echo -e "Nama: Andi Simulasi\nAlamat: Jalan Testing No. 123\nTTL: 01 Januari 1990\nStatus: Aktif (simulasi)"
      ;;
    10)
      read -p "Pesan kamu: " pesan
      echo -e "${green}GusOfc menjawab:${nc} Tenang aja, $user. Semua akan baik-baik saja!"
      ;;
    11)
      echo -e "${purple}Bot GusOfc v2.0"
      echo -e "Dibuat pada: $(date '+%Y-%m-%d')"
      echo -e "Owner: GUSxOFC"
      echo -e "NOTE: HARGAILAH KARYA INI${nc}"
      ;;
    0)
      echo -e "${red}Keluar dari bot. Terima kasih!${nc}"
      exit
      ;;
    *)
      echo -e "${red}Pilihan tidak valid.${nc}"
      ;;
  esac

done
