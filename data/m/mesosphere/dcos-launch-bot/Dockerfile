FROM python:3.5-slim  
COPY . /app  
WORKDIR /app  
RUN apt-get update && \  
apt-get install -y git libffi-dev && \  
rm -rf /var/lib/apt/lists/*  
RUN pip3 install -r requirements.txt  

