FROM tiangolo/uwsgi-nginx:latest  
  
MAINTAINER Cássio R Eskelsen<eskelsen@gmail.com>  
  
RUN apt-get update -y && apt-get install -y \  
software-properties-common \  
python-software-properties \  
build-essential \  
python-dev \  
python-numpy \  
libspatialite-dev \  
sqlite3 \  
libpq-dev \  
libcurl4-gnutls-dev \  
libproj-dev \  
libxml2-dev \  
libgeos-dev \  
libspatialite-dev \  
gdal-bin \  
libgdal-dev \  
libgdal1-dev \  
python-gdal \  
wget \  
postgis \  
python-pyinotify \  
uwsgi-plugin-python \  
unzip  
  
RUN pip install flask  
RUN pip install flask-security  
RUN pip install flask-admin  
  
COPY requeriments.txt /tmp/requeriments.txt  
COPY upload_100m.conf /etc/nginx/conf.d/  
COPY nginx.conf /etc/nginx/conf.d/  
COPY watcher.ini /etc/watcher.ini  
COPY ./app /app  
  
RUN pip install -r /tmp/requeriments.txt  
  
RUN mkdir -p /opt/geoserver/data_dir  
RUN mkdir -p /media/imagens_upload

