import requests

def shodan_lookup(query, shodan_api):
    url = f"https://api.shodan.io/shodan/host/search?key={shodan_api}&query={query}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json()
        for match in results['matches']:
            print(f"IP: {match['ip_str']} | Ports: {match.get('port', 'N/A')}")
    else:
        print("❌ Error fetching data from Shodan.")

def virustotal_scan(url, vt_api):
    headers = {"x-apikey": vt_api}
    scan_url = "https://www.virustotal.com/api/v3/urls"

    response = requests.post(scan_url, headers=headers, data={"url": url})
    if response.status_code == 200:
        scan_id = response.json()['data']['id']
        result_url = f"https://www.virustotal.com/gui/url/{scan_id}"
        print(f"✅ VirusTotal Scan Complete: {result_url}")
    else:
        print("🚨 VirusTotal Scan Failed.")

def hunter_email_lookup(domain, hunter_api):
    """Find emails associated with a domain"""
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={hunter_api}"
    response = requests.get(url)

    if response.status_code == 200:
        emails = response.json()['data']['emails']
        for email in emails:
            print(f"📧 Found Email: {email['value']} (Confidence: {email['confidence']}%)")
    else:
        print("❌ No emails found.")
