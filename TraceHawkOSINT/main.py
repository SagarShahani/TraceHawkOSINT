# main.py

import argparse
import os
from modules import username_check, email_breach, domain_lookup, ip_lookup
from modules.report_generator import ReportGenerator
from pyfiglet import figlet_format
from termcolor import cprint

def banner():
    cprint(figlet_format("TraceHawk", font="slant"), "cyan")
    print("🦅 Open Source Intelligence Toolkit by Sagar\n")

def main():
    parser = argparse.ArgumentParser(
        description="🦅 TraceHawkOSINT - Open Source Intelligence Recon Toolkit"
    )
    parser.add_argument("--all", action="store_true", help="Run all modules together")
    parser.add_argument("--username", help="Check username across platforms")
    parser.add_argument("--email", help="Check email breach & validity")
    parser.add_argument("--domain", help="Get WHOIS and DNS records of a domain")
    parser.add_argument("--ip", help="Lookup location and ISP info for IP address")
    parser.add_argument("--report", help="Generate PDF report (e.g. --report output.pdf)")

    args = parser.parse_args()

    banner()

    # Ensure reports/ folder exists
    if args.report:
        if not os.path.exists("reports"):
            os.makedirs("reports")
        args.report = os.path.join("reports", args.report)

    print("🔎 TraceHawkOSINT Recon Starting...\n")

    report = ReportGenerator(args.report) if args.report else None

    # If --all is set, run everything provided
    if args.all:
        if args.username:
            output = username_check.check_username(args.username)
            if report:
                report.add_section("Username Recon", output)

        if args.email:
            output = email_breach.check_email(args.email)
            if report:
                report.add_section("Email Recon", output)

        if args.domain:
            output = domain_lookup.lookup_domain(args.domain)
            if report:
                report.add_section("Domain Recon", output)

        if args.ip:
            output = ip_lookup.lookup_ip(args.ip)
            if report:
                report.add_section("IP Recon", output)

    # If --all not used, run only selected modules
    else:
        if args.username:
            output = username_check.check_username(args.username)
            if report:
                report.add_section("Username Recon", output)

        if args.email:
            output = email_breach.check_email(args.email)
            if report:
                report.add_section("Email Recon", output)

        if args.domain:
            output = domain_lookup.lookup_domain(args.domain)
            if report:
                report.add_section("Domain Recon", output)

        if args.ip:
            output = ip_lookup.lookup_ip(args.ip)
            if report:
                report.add_section("IP Recon", output)

    if report:
        report.save()
        print(f"\n[+] PDF Report saved as {args.report}")

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()

