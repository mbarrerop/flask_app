# Netflix Flask App

This project is used to upload movie files to Google and obtain upload results. This load can be multiple or simple. The data can be fully recovered or paged. This can be done from a python script or invoked as a Rest API.

## Content

- [Requirements](#requisitos)
- [Instalation](#instalación)
- [Use](#uso)
- [License](#licencia)

## Requirements

- docker https://docs.docker.com/get-docker/
- requests https://pip.pypa.io/en/stable/installing/
- Python 3.10 https://www.python.org/downloads/release/python-31011/
- All libraries in requirements.txt

## Instalation

1. Clone or download this repository.

```bash
git clone https://github.com/mbarrerop/flask_app.git
```

2. Install requests library.

```bash
# If you have a pip in you os
pip install requests
```

otherwise follow the instructions on the official pip page: https://pip.pypa.io/en/stable/installing/

3.  Enviroment variables.

    Before running this project, you must configure some environment variables. Follow these steps to do it:

        1. Create a file called `.env` in the root of your project if it does not exist

        2. Open the `.env` file and define your environment variables in the format `VARIABLE_NAME=value`. For example:
            API_KEY=secret_key
            DEBUG=True

    For this project you must configure the following Google Storage API variables. The file structure can be found in the env_example file located at the root of the repository.

    ```bash

        # Database
        DRIVER_NAME=postgresql
        DB_NAME=name
        DB_USER=user
        DB_PASS=pass
        DB_HOST=host
        DB_PORT=port

        # Debugging
        DEBUG=True

        PROJECT_ID=project_id
        PRIVATE_KEY_ID=key
        PRIVATE_KEY=private_key
        CLIENT_EMAIL=client_email
        CLIENT_ID=33344
        AUTH_URI=https://accounts.google.com/o/oauth2/auth
        TOKEN_URI=https://oauth2.googleapis.com/token
        AUTH_PROVIDER=https://www.googleapis.com/oauth2/v1/certs
        CLIENT=client
        UNIVERSE_DOMAIN=googleapis.com

        BUCKET_NAME=movies_app
        BUCKET_LOCATION=US
        MOVIES_FILE_NAME=netflix_titles.csv

        # ThreadPool
        THREADPOOL=3
    ```

    Once the .env file is configured in the directory where the project is located, you can proceed to launch the application

4.  Building and Deploy
    ```bash
    # Building the image
    docker build -t flask-app .
    ```
    ```bash
    # Once you have building your application image, you can deploy it using Docker.
    docker run -d -p 5000:5000 flask-app
    ```

## Use

1. At the root of the project there is a script.py file. This file will allow you to run the API via command line. Go to the path where the cloned project is located and find the script.py file.
2. Locate from your operating system console where the file is located.

   ```bash
   # Use this command to find help
   python3 script.py -h
   ```

3. To upload files you must provide the url of the file upload point and the path where the file you want to upload is located locally as shown below.
   ```bash
   # Script structure to save files in Google Cloud Storage
   python3 script.py --url_save  http://0.0.0.0:5000/admin/save-movies --file_paths "/dir/path/one.csv" "/dir/path/two.csv"
   # Example
   python3 script.py --url_save  http://0.0.0.0:5000/admin/save-movies --file_paths "/home/miguel/Downloads/netflix_titles.csv" "/home/miguel/Downloads/netflix_titles_1.csv"
   ```
   ```bash
   # Example of a response when a file could or could not be loaded
   {'result': [{'file_name': 'netflix_titles.csv', 'uploaded': True}], 'status_code': 200}
   'The file /home/miguel/Downloads/netflix_titles1.csv is not found in the specified path.'
   ```
4. To recover a file you must provide the url to list the files. Optionally, if you wish, you can add parameters such as <span style="color: red;">page</span> to divide by page the results or obtain a specific file through the <span style="color: red;">file_name</span> parameter. If you do not provide any file name, it will default to the netflix_titles.csv file.

   ```bash
   # Script structure to recover file data from Google Cloud Storage
   python3 script.py --url_get_file  http://127.0.0.1:5000/movies/list

   # Script if you get results by pages
   python3 script.py --url_get_file  http://127.0.0.1:5000/movies/list?page=1

   # Script if you get results by pages and specific file
   python3 script.py --url_get_file  http://127.0.0.1:5000/movies/list?page=1&file_name=netflix_titles_1.csv

   # Script to save a data obtained from the enpoint. You must set --save_file as True and a correct path from you local system
   python3 script.py --url_get_file  http://127.0.0.1:5000/movies/list?file_name=netflix_titles_1.csv --save_file True --save_path /home/miguel
   ```

## License

This project is distributed under the [MIT License](LICENSE). You can find more details in the [LICENSE](LICENSE) file.

The MIT License is an open-source license that allows for free distribution and modification of the software, provided that the copyright notice is included in all copies. It is one of the most permissive and widely used licenses in the world of open-source software.

**Summary of the MIT License:**

- You can use, copy, modify, merge, publish, distribute, sublicense, and/or sell the software.
- You must include a copy of the copyright notice in all copies or substantial portions of the software.
- The software is provided "as is," without any warranties.

Be sure to refer to the [LICENSE](LICENSE) file for the full text of the MIT License and legal details. If you wish to use a different license, make sure to provide a link to the full text of that license instead of the MIT License.
