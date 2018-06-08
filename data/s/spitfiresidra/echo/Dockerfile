FROM debian:jessie  
MAINTAINER Amo Chen <spitfire.sidra@gmail.com>  
  
ADD https://bootstrap.pypa.io/get-pip.py /  
RUN apt-get update && apt-get install -y python && rm -rf /var/lib/apt/lists/*
&& \  
python get-pip.py  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
  
ENTRYPOINT python web.py  

