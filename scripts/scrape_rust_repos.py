import requests
import json
import os

def get_repositories(page_number, per_page=50):
    url = "https://crates.io/api/v1/crates"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.6',
        'Referer': 'https://crates.io/',
        'Cookie': 'cargo_session=' + os.environ.get('SESSION_COOKIE')
    }
    params = {
        'page': page_number,
        'per_page': per_page,
        'sort': 'downloads'
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        crates = json.loads(response.text)['crates']
        return [crate['repository'] for crate in crates if crate['repository']]
    else:
        print(f"Failed to fetch the page with status code: {response.status_code}")
        return None

total_repositories = 10000
per_page = 50
page_number = 1

with open('repositories.txt', 'w') as file:
    while total_repositories > 0:
        print(f"Scraping page {page_number}...")
        repositories = get_repositories(page_number, per_page)
        if repositories:
            for repo in repositories:
                file.write(repo + '\n')
            total_repositories -= len(repositories)
            print(f"Found {len(repositories)} repositories on page {page_number}. Remaining: {total_repositories}")
        else:
            print(f"Failed to fetch repositories on page {page_number}.")

        page_number += 1

print("Scraping completed!")
