import requests
import argparse
import json
import os

parser = argparse.ArgumentParser(description='Script to load files in an endpoint')
parser.add_argument('--url_save', help='URL endpoint to save files')
parser.add_argument('--file_paths', nargs='+', help='File paths')
parser.add_argument('--url_get_file', help='URL endpoint to get file data')
parser.add_argument('--save_path', help='Local path to save the data')
parser.add_argument('--save_file', help='True if you want save the result file')
args = parser.parse_args()

def send_files(url, file_paths):
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f'The file {file_path} is not found in the specified path.')
        else:
            with open(file_path, 'rb') as file:
                files = {'files': (os.path.basename(file_path), file)}
                response = requests.post(url, files=files)

            print(f'File: {file_path}, Status Code: {response.status_code}')
            print(response.json())

def get_data_file(url, save=False, save_path=None):
    response = requests.get(url)
    print(args.url_get_file, args.save_path)
    if save and save_path:
        file_route = os.path.join(save_path, "netflix_titles.json")
        with open(file_route, 'w') as archivo_json:
            json.dump(response.json(), archivo_json, indent=4)
        print(f'File saved in: {file_route}')
    else:
        
        print(response.json())
     
if args.url_save and args.file_paths:
    send_files(args.url_save, args.file_paths)
    
if args.url_get_file:
    if args.save_file and args.save_path:
        get_data_file(args.url_get_file, args.save_file, args.save_path)
    else:
        get_data_file(args.url_get_file)    
    
