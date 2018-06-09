FROM python:2-slim  
MAINTAINER Paulius Masiliunas <info@pauliaus.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN set -ex \  
&& buildDeps=' \  
python-software-properties \  
libzmq-dev \  
libmapnik-dev \  
mapnik-utils \  
python-mapnik \  
libjpeg-dev \  
zlib1g-dev \  
gdal-bin \  
libgdal-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt /usr/src/app/  
RUN pip install -r requirements.txt  
  
COPY tilestache.cfg /etc/tilestache/tilestache.cfg  
COPY gunicorn_config.py /etc/gunicorn/config.py  
  
EXPOSE 8080  
CMD gunicorn --config '/etc/gunicorn/config.py'
"TileStache:WSGITileServer('/etc/tilestache/tilestache.cfg')"

