# Using 3.10 python enviroment
FROM python:3.10-slim

# Work dir
WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

# copy content /src
COPY . .

# Installation requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Port expose
EXPOSE 5000

# Execution flask app
CMD gunicorn main:app -b 0.0.0.0:5000 --max-requests 100 --access-logfile - --error-logfile - --log-level info