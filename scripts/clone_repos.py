import requests
import subprocess
import os
import time

def get_latest_release(repo_url, retries=2, delay=1):
    for attempt in range(retries):
        parts = repo_url.split('/')
        owner = parts[-2]
        repo_name = parts[-1]
        api_url = f'https://api.github.com/repos/{owner}/{repo_name}/releases/latest'
        headers = {'Authorization': 'token'}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json()['tarball_url']
        else:
            print(f"Attempt {attempt + 1}: Failed to fetch the latest release for {repo_url}. Status code: {response.status_code}. Retrying in {delay} seconds...")
            time.sleep(delay)

    print(f"Failed to fetch the latest release for {repo_url} after {retries} attempts.")
    with open('failed.txt', 'a') as file:
        file.write(repo_url + '\n')
    return None

def clone_repo(tarball_url, destination):
    subprocess.run(['wget', tarball_url, '-O', destination])
    subprocess.run(['tar', '-xzvf', destination, '-C', 'repos'])

def main():
    os.makedirs('repos', exist_ok=True)

    with open('repositories.txt', 'r') as file:
        repos = file.readlines()
        total_repos = len(repos)
        for idx, line in enumerate(repos):
            repo_url = line.strip()
            print(f"Cloning the latest release for {repo_url} ({idx + 1}/{total_repos})...")

            tarball_url = get_latest_release(repo_url)
            if tarball_url:
                destination = os.path.join('cloned_repos', os.path.basename(repo_url) + '.tar.gz')
                os.makedirs(os.path.dirname(destination), exist_ok=True)
                clone_repo(tarball_url, destination)
                print(f"Successfully cloned {repo_url} to 'repos' folder")
                with open('downloaded.txt', 'a') as file:
                    file.write(repo_url + '\n')
            else:
                print(f"Failed to clone {repo_url}")

if __name__ == "__main__":
    main()
