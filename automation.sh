#!/bin/bash

# Check if the user provided the target domain
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 target.com"
    exit 1
fi

# Assign the target domain from the command-line argument
TARGET="$1"

# Create a directory to store the output
OUTPUT_DIR="${TARGET}_subdomains"
mkdir -p "$OUTPUT_DIR"
echo "[+] Results will be saved in $OUTPUT_DIR"

# Exporting PDCP Api key
echo "[X] Exporting PDCP_API_KEY ..."
export PDCP_API_KEY=b235613b-dc7b-43ef-96cf-8c58e8b692b9

# Hackertarget.com enumeration
echo "[*] Fetching subdomains from hackertarget.com..."
curl -s "https://api.hackertarget.com/hostsearch/?q=$TARGET" | cut -d, -f1 | sort -u > "$OUTPUT_DIR/hackertarget.txt"

# crt.sh enumeration
echo "[*] Fetching subdomains from crt.sh..."
curl -s "https://crt.sh/?q=%25.$TARGET&output=json" | jq -r '.[] | .name_value' | sed 's/\*\.//g' | sort -u > "$OUTPUT_DIR/crtsh.txt"

# rapiddns.io enumeration
echo "[*] Fetching subdomains from rapiddns.io..."
curl -s "https://rapiddns.io/subdomain/$TARGET?full=1#result" | grep -e "<td>.*$TARGET</td>" | grep -oP '(?<=<td>)[^<]+' | sort -u > "$OUTPUT_DIR/rapiddnsio.txt"

# AlienVault OTX enumeration
echo "[*] Fetching subdomains from AlienVault OTX..."
curl -s "https://otx.alienvault.com/api/v1/indicators/domain/$TARGET/url_list?limit=100&page=1" | grep -o '"hostname": *"[^"]*' | sed 's/"hostname": "//' | sort -u > "$OUTPUT_DIR/alienvault.txt"

# subdomain.center enumeration
echo "[*] Fetching subdomains from subdomain.center..."
curl -s "https://api.subdomain.center/?domain=$TARGET" | jq -r '.[]' | sort -u > "$OUTPUT_DIR/subcenter.txt"

# Subfinder enumeration
echo "[*] Running Subfinder..."
subfinder -d "$TARGET" -t 200 -silent -all -recursive -o "$OUTPUT_DIR/subfinder.txt"

# Sublist3r enumeration
echo "[*] Running Sublist3r..."
sublist3r -d "$TARGET" -t 20 -o "$OUTPUT_DIR/sublist3r.txt"

# Chaos enumeration
echo "[*] Fetching subdomains from Chaos..."
chaos -d "$TARGET" -silent > "$OUTPUT_DIR/chaos.txt"

# Combine all subdomains and sort them uniquely into a final file
echo "[+] Combining results into $OUTPUT_DIR/all_subdomains.txt..."
cat "$OUTPUT_DIR"/*.txt | sort -u > "$OUTPUT_DIR/all_subdomains.txt"

echo "[+] Subdomain enumeration completed. Results saved in $OUTPUT_DIR"

