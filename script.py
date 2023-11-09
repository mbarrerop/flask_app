import requests
import argparse
import os

parser = argparse.ArgumentParser(description='Script to load a file in a endpoint.')
parser.add_argument('url', help='URL enpoint to send the netflix_titles.csv')
parser.add_argument('file_path', help='File path ')

# Help
parser.add_argument('--help', action='help', help='Muestra este menú de ayuda')

args = parser.parse_args()

# Backend post file
url = args.url
file_path = args.file_path
    
# Reading the file
if not os.path.exists(file_path):
    print(f'The file {file_path} is not found in the specified path.')
else:
    with open(file_path, 'rb') as file:
        # Building the post request
        files = {'file': (file_path, file)}

        # Making the request
        response = requests.post(url, files=files)

    # Printing the response from the first endpoint
    print(response.status_code)
    print(response.json())