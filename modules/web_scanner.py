import requests
import json

def detect_waf(url):
    """Detect Web Application Firewalls by analyzing HTTP headers"""
    try:
        response = requests.get(url)
        headers = response.headers

        waf_signatures = {
            "Cloudflare": "cf-ray",
            "Akamai": "akamai",
            "Incapsula": "incap_ses",
            "Sucuri": "sucuri-cloudproxy",
            "AWS WAF": "x-amzn-waf",
        }

        for waf, signature in waf_signatures.items():
            if any(signature in value.lower() for key, value in headers.items()):
                print(f"🔴 WAF Detected: {waf}")
                return waf
        print("✅ No WAF detected.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def cms_fingerprint(url):
    """Detect CMS (WordPress, Joomla, Drupal, etc.)"""
    cms_patterns = {
        "WordPress": "/wp-admin/",
        "Joomla": "/administrator/",
        "Drupal": "/core/",
    }

    for cms, path in cms_patterns.items():
        response = requests.get(url + path)
        if response.status_code == 200:
            print(f"🔍 Detected CMS: {cms}")
            return cms
    print("❓ Unknown CMS")

def scan_ssl(url):
    """Check SSL certificate details"""
    try:
        response = requests.get(f"https://{url}", timeout=5, verify=True)
        cert = response.raw.connection.sock.getpeercert()
        print(f"🔒 SSL Certificate Details: {json.dumps(cert, indent=4)}")
    except requests.exceptions.SSLError:
        print("🚨 SSL Certificate Invalid or Not Found!")

def scan_website(url):
    print(f"🌐 Scanning Website: {url}\n")
    detect_waf(url)
    cms_fingerprint(url)
    scan_ssl(url)
