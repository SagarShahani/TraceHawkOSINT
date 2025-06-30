# 🦅 TraceHawkOSINT

A powerful and beginner-friendly Open Source Intelligence (OSINT) toolkit written in Python — developed by **Sagar Shahani**.

TraceHawkOSINT allows investigators, cybersecurity students, and enthusiasts to gather publicly available data on usernames, emails, domains, and IP addresses. It generates a comprehensive PDF report with the results.

---

## 📌 Features

- 🔍 **Username Recon** — Checks multiple social platforms  
- 📧 **Email Verification** — Disposable, risky, breached status  
- 🌐 **Domain Lookup** — WHOIS + DNS (A, MX, TXT records)  
- 📡 **IP Geolocation** — ISP, ASN, City, Country  
- 🧾 **PDF Report** — Clean, auto-generated PDF reports  
- 📁 **Auto-Saves to** `/reports/` folder  
- 🚀 **Supports `--all` mode** for full recon in one go  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SagarShahani/TraceHawkOSINT.git
cd TraceHawkOSINT

2. Set Up Environment (Optional but Recommended)
python3 -m venv myenv
source myenv/bin/activate  # or .\myenv\Scripts\activate on Windows

3. Install Dependencies
pip install -r requirements.txt

Usage
python3 main.py --all --username <username> --email <email> --domain <domain> --ip <ip> --report <report_name.pdf>
