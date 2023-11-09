import requests
import argparse
import os

parser = argparse.ArgumentParser(description='Script to load a file in an endpoint')
parser.add_argument('--url', help='URL endpoint to send the netflix_titles.csv')
parser.add_argument('--file_path', help='File path')

args = parser.parse_args()

if not os.path.exists(args.file_path):
    print(f'The file {args.file_path} is not found in the specified path.')
else:
    with open(args.file_path, 'rb') as file:
        files = {'file': (os.path.basename(args.file_path), file)}
        response = requests.post(args.url, files=files)

    print(response.status_code)
    print(response.json())