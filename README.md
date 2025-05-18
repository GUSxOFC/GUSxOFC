#!/bin/bash

# GusOfc - Version 1.0
# Owner: GUSxOFC

# Warna
blue='\033[1;34m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
nc='\033[0m'

banner() {
    clear
    echo -e "${blue}"
    echo "██████╗ ██╗   ██╗███████╗ ██████╗ ███████╗ ██████╗"
    echo "██╔══██╗██║   ██║██╔════╝██╔════╝ ██╔════╝██╔═══██╗"
    echo "██║  ██║██║   ██║█████╗  ██║  ███╗█████╗  ██║   ██║"
    echo "██║  ██║██║   ██║██╔══╝  ██║   ██║██╔══╝  ██║   ██║"
    echo "██████╔╝╚██████╔╝███████╗╚██████╔╝███████╗╚██████╔╝"
    echo "╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ "
    echo -e "${nc}Version 1.0 by ${yellow}GUSxOFC${nc}"
    echo
}

menu() {
    echo -e "${green}[1] IP - Info IP address"
    echo -e "[2] Scan - Scan website"
    echo -e "[3] Search - Jejak digital (via DuckDuckGo)"
    echo -e "[4] Info Henphone - Nomor WA Info"
    echo -e "[0] Exit${nc}"
    echo
    read -p "Pilih menu: " choice
    case $choice in
        1) ip_info ;;
        2) scan_web ;;
        3) digital_trace ;;
        4) nomor_info ;;
        0) exit ;;
        *) echo -e "${red}Pilihan tidak valid!${nc}" ; sleep 1 ; menu ;;
    esac
}

ip_info() {
    echo -e "${yellow}Mendapatkan informasi IP publik...${nc}"
    curl -s ipinfo.io | jq
    echo
    read -p "Tekan enter untuk kembali ke menu..."
    banner; menu
}

scan_web() {
    read -p "Masukkan URL (contoh: https://google.com): " url
    echo -e "${yellow}Melakukan scan pada $url...${nc}"
    curl -I "$url"
    echo
    read -p "Tekan enter untuk kembali ke menu..."
    banner; menu
}

digital_trace() {
    read -p "Masukkan kata kunci (nama, username, dll): " keyword
    echo -e "${yellow}Mencari di DuckDuckGo...${nc}"
    curl -s "https://lite.duckduckgo.com/lite/?q=${keyword// /+}" | html2text | head -n 20
    echo
    read -p "Tekan enter untuk kembali ke menu..."
    banner; menu
}

nomor_info() {
    read -p "Masukkan nomor HP (contoh: 081234567890): " nomor
    echo -e "${yellow}Cek info nomor...${nc}"
    if [[ $nomor =~ ^08[0-9]{8,11}$ ]]; then
        kode=${nomor:0:4}
        case $kode in
            0811|0812|0813) echo "Provider: Telkomsel" ;;
            0821|0822|0852) echo "Provider: Telkomsel" ;;
            0856|0857|0858) echo "Provider: Indosat" ;;
            0817|0818|0819) echo "Provider: XL" ;;
            0895|0896|0897|0898|0899) echo "Provider: Tri" ;;
            *) echo "Provider tidak dikenali" ;;
        esac
    else
        echo -e "${red}Format nomor salah!${nc}"
    fi
    echo
    read -p "Tekan enter untuk kembali ke menu..."
    banner; menu
}

# Install dependencies
dependencies() {
    echo -e "${green}Menginstall dependencies...${nc}"
    pkg install curl jq html2text -y > /dev/null 2>&1
}

# Eksekusi
dependencies
banner
menu
