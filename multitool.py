import argparse
import json
import threading
from modules import (
    ip_recon,
    port_scanner,
    web_scanner,
    breach_checker,
    osint,
    dark_web,
    reporting
)

# Load API keys
with open("config.json", "r") as f:
    config = json.load(f)

def run_command(args):
    if args.command == "whois":
        ip_recon.whois_lookup(args.domain)
    elif args.command == "scan-ip":
        port_scanner.scan_ports(args.ip, args.ports)
    elif args.command == "webscan":
        web_scanner.scan_website(args.url)
    elif args.command == "breach-check":
        breach_checker.check_breach(args.email, config["hibp_api"])
    elif args.command == "shodan":
        osint.shodan_lookup(args.query, config["shodan_api"])
    elif args.command == "darkweb":
        dark_web.search_onion(args.keyword)
    elif args.command == "report":
        reporting.generate_report(args.output_format)
    else:
        print("Invalid command!")

def main():
    parser = argparse.ArgumentParser(description="MultiTool - Advanced OSINT & Security Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    parser_ip = subparsers.add_parser("whois", help="Perform WHOIS lookup")
    parser_ip.add_argument("domain", help="Domain to check")

    parser_scan = subparsers.add_parser("scan-ip", help="Advanced IP Port Scanning")
    parser_scan.add_argument("ip", help="Target IP")
    parser_scan.add_argument("--ports", default="1-65535", help="Port range (default: full scan)")

    parser_web = subparsers.add_parser("webscan", help="Run advanced web security scan")
    parser_web.add_argument("url", help="Target website")

    parser_breach = subparsers.add_parser("breach-check", help="Check data breaches")
    parser_breach.add_argument("email", help="Email to check")

    parser_osint = subparsers.add_parser("shodan", help="Shodan search")
    parser_osint.add_argument("query", help="Search query")

    parser_darkweb = subparsers.add_parser("darkweb", help="Search Dark Web for leaks")
    parser_darkweb.add_argument("keyword", help="Keyword to search")

    parser_report = subparsers.add_parser("report", help="Generate reports")
    parser_report.add_argument("output_format", choices=["json", "md", "html"], help="Report format")

    args = parser.parse_args()

    thread = threading.Thread(target=run_command, args=(args,))
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()