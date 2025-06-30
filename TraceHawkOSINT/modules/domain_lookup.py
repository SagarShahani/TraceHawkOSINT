# modules/domain_lookup.py
import whois
import dns.resolver

def lookup_domain(domain):
    print(f"[+] Performing WHOIS lookup for: {domain}\n")

    try:
        w = whois.whois(domain)
        print(f"Registrar      : {w.registrar}")
        print(f"Creation Date  : {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers   : {w.name_servers}")
        print()
    except Exception as e:
        print(f"[!] WHOIS Error: {e}\n")

    print(f"[+] Fetching DNS records for: {domain}\n")

    record_types = ["A", "MX", "TXT"]
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"--- {record} Records ---")
            for rdata in answers:
                print(f"{rdata}")
            print()
        except Exception:
            print(f"[!] No {record} record found.\n")
