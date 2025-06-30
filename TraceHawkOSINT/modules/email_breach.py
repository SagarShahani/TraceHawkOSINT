import requests

API_KEY = "fc32cf55b11f472126232058db5053be9d9475a5"

def check_email(email):
    print(f"[+] Checking email status for: {email}")
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={API_KEY}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()["data"]
            print(f"\n[✓] Email: {result['email']}")
            print(f"[✓] Status: {result['status']}")
            print(f"[✓] Score: {result['score']}% confidence")
            print(f"[✓] Result: {result['result']}")
            print(f"[✓] SMTP Check: {'Yes' if result['smtp_check'] else 'No'}")
            print(f"[✓] Sources Found: {len(result['sources'])}")
            
            if result['sources']:
                print("\n[+] Sources:")
                for source in result['sources']:
                    print(f" - {source['uri']} (last seen: {source['last_seen']})")
        else:
            print(f"[!] API error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[!] Exception occurred: {e}")
