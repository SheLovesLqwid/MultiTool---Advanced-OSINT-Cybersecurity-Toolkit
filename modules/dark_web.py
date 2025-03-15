import requests

def search_onion(keyword):
    url = f"https://darksearch.io/api/search?query={keyword}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json()
        for result in results['data']:
            print(f"Dark Web Result: {result['title']} - {result['link']}")
    else:
        print("No results found.")
