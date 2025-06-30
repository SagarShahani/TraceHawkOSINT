# modules/ip_lookup.py

import requests

def lookup_ip(ip):
    print(f"[+] Looking up IP: {ip}\n")

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = response.json()

        info = {
            "IP": data.get("ip", "N/A"),
            "Hostname": data.get("hostname", "N/A"),
            "City": data.get("city", "N/A"),
            "Region": data.get("region", "N/A"),
            "Country": data.get("country", "N/A"),
            "Location": data.get("loc", "N/A"),
            "Org/ISP": data.get("org", "N/A"),
            "ASN": data.get("asn", {}).get("asn", "N/A") if isinstance(data.get("asn"), dict) else "N/A",
            "Timezone": data.get("timezone", "N/A")
        }

        for key, value in info.items():
            print(f"{key:<12}: {value}")

        # Return list of strings for PDF
        return [f"{key}: {value}" for key, value in info.items()]

    except Exception as e:
        print(f"[ERROR] Could not lookup IP: {e}")
        return [f"[ERROR] Could not lookup IP: {e}"]

