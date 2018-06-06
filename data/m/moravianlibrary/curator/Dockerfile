FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y python-pip nano cron && pip install
elasticsearch-curator && rm -rf /var/lib/apt/lists/*  

