FROM ubuntu:precise  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update \  
&& apt-get install -y -q python-software-properties python-pip libzmq-dev \  
&& add-apt-repository -y ppa:mapnik/v2.2.0 \  
&& apt-get update \  
&& apt-get install -y -q libmapnik libmapnik-dev mapnik-utils python-mapnik \  
&& apt-get install -y -q libjpeg-dev zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
COPY requirements.txt /usr/src/app/  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
ONBUILD COPY . /usr/src/app  
  
CMD gunicorn -b 0.0.0.0:8080 "TileStache:WSGITileServer('tilestache.cfg')"  
  

