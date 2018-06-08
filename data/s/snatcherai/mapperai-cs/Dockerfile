# Dockerfile  
# FROM directive instructing base image to build upon  
# FROM python:3.6-jessie  
FROM ubuntu:latest  
  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y python3-pip python3-dev \  
&& cd /usr/local/bin \  
&& ln -s /usr/bin/python3 python \  
&& pip3 install --upgrade pip  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get install -y python3-numpy gdal-bin libgdal-dev python3-gdal
python3-rasterio  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
# done!  

