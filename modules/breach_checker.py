import requests
import re

def check_breach(email, hibp_api):
    headers = {"hibp-api-key": hibp_api}
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        breaches = response.json()
        print(f"Breaches found for {email}:")
        for breach in breaches:
            print(f"- {breach['Name']} (Date: {breach['BreachDate']})")
    elif response.status_code == 404:
        print("No breaches found.")

def check_pastebin_leaks(keyword):
    url = f"https://psbdmp.ws/api/search/{keyword}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pastes = response.json()
        for paste in pastes:
            print(f"Found Paste: {paste['id']} - {paste['title']}")
