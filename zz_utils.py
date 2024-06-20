import os
import requests
from bs4 import BeautifulSoup

import glob

def download_files(url, download_folder):
    # Create the directory for downloaded files if it does not exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        # Get the page content
        response = requests.get(url)
        response.raise_for_status()  # will raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return


    # Find all the .csv.tar links
    links = soup.find_all('a', href=True)
    tar_links = [link['href'] for link in links if link['href'].endswith('.csv.tar')] # TAKE THE CSV FORMAT

    print(f'Found {len(tar_links)} files to download:')
    # remove duplicates
    tar_links = list(dict.fromkeys(tar_links))

    for link in tar_links:
        # Construct the full URL for the file
        full_url = url + link
        file_name = link.split('/')[-1] # [-1] gets the last part of the URL which is the file name
        file_path = os.path.join(download_folder, file_name)

        # Download the file
        print(f'Downloading {file_name}...')
        r = requests.get(full_url)
        with open(file_path, 'wb') as f:
            f.write(r.content)

def extract_files(source_folder):
    import tarfile
    # Check all files in the directory
    for filename in os.listdir(source_folder):
        if filename.endswith('.tar'):
            file_path = os.path.join(source_folder, filename)
            print(f'Extracting {filename}...')
            with tarfile.open(file_path, 'r:') as tar:
                tar.extractall(path=source_folder)
            # Optionally, uncomment the next line to delete the tar file after extraction
            os.remove(file_path)



def get_neighboring_rows(df_temp, condition_temp, before=10, after=10):
    # Get the indices of the rows that meet the condition

    df = df_temp.copy()
    condition = condition_temp.copy()

    df = df.reset_index(drop=True)
    condition = condition.reset_index(drop=True)

    condition_indices = df[condition].index
    #print(condition_indices)

    # Find the neighbor rows (before and after)
    neighbor_indices = []

    for idx in condition_indices:
        start_idx = max(idx - before, 0)
        end_idx = min(idx + after, len(df) - 1)
        neighbor_indices.extend(range(start_idx, end_idx + 1))

    # Remove duplicates
    neighbor_indices = list(set(neighbor_indices))

    # Get the neighboring rows
    neighboring_rows = df.iloc[neighbor_indices].sort_index()

    return neighboring_rows
