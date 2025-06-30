# modules/username_check.py

import requests

def check_username(username):
    print(f"[+] Checking username: {username}\n")
    
    sites = [
        f"https://github.com/{username}",
        f"https://twitter.com/{username}",
        f"https://instagram.com/{username}",
        f"https://reddit.com/user/{username}",
        f"https://www.tiktok.com/@{username}",
        f"https://www.pinterest.com/{username}/",
        f"https://www.medium.com/@{username}",
        f"https://www.quora.com/profile/{username}",
        f"https://www.deviantart.com/{username}",
        f"https://steamcommunity.com/id/{username}"
    ]

    results = []

    for url in sites:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                msg = f"[FOUND]      {url}"
            elif response.status_code == 404:
                msg = f"[NOT FOUND]  {url}"
            else:
                msg = f"[UNKNOWN]    {url} - Status: {response.status_code}"
        except requests.RequestException as e:
            msg = f"[ERROR]       {url} - {e}"
        
        print(msg)
        results.append(msg)

    return results

