import whois
import socket
import requests

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"WHOIS Data for {domain}:\n", w)
    except Exception as e:
        print(f"Error: {e}")

def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
        print(f"Reverse DNS for {ip}: {result[0]}")
    except socket.herror:
        print("No reverse DNS record found.")

def asn_lookup(ip):
    url = f"https://api.hackertarget.com/aslookup/?q={ip}"
    response = requests.get(url)
    print(response.text)
