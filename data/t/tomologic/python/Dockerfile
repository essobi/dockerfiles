FROM python:2-slim  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN apt-get update && \  
apt-get install -y build-essential && \  
pip install --no-cache-dir -r requirements.txt && \  
apt-get remove -y --purge build-essential && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ONBUILD COPY . /usr/src/app  

