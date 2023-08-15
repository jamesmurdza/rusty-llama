import subprocess
import os
import time

def get_master_tarball_url(repo_url):
    parts = repo_url.split('/')
    owner = parts[-2]
    repo_name = parts[-1]
    return f'https://github.com/{owner}/{repo_name}/archive/refs/heads/master.tar.gz'

def clone_repo(tarball_url, destination):
    subprocess.run(['wget', tarball_url, '-O', destination])
    subprocess.run(['tar', '-xzvf', destination, '-C', 'repos'])

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    print("Current repos size: ", total_size)
    return total_size

def main():
    os.makedirs('repos', exist_ok=True)
    MAX_SIZE_MB = 500
    MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024

    with open('repositories.txt', 'r') as file:
        repos = file.readlines()
        total_repos = len(repos)
        for idx, line in enumerate(repos):
            repo_url = line.strip()
            print(f"Cloning the master branch for {repo_url} ({idx + 1}/{total_repos})...")

            tarball_url = get_master_tarball_url(repo_url)
            destination = os.path.join('cloned_repos', os.path.basename(repo_url) + '.tar.gz')
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            clone_repo(tarball_url, destination)
            print(f"Successfully cloned {repo_url} to 'repos' folder")
            with open('downloaded2.txt', 'a') as file:
                file.write(repo_url + '\n')

            if get_directory_size('repos') >= MAX_SIZE_BYTES:
                print(f"Reached {MAX_SIZE_MB} megabytes of cloned repos. Stopping process.")
                break

if __name__ == "__main__":
    main()
