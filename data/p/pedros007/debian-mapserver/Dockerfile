FROM pedros007/debian-gdal:2.2.3  
MAINTAINER Peter Schmitt "pschmitt@gmail.com"  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y \  
nginx supervisor \  
build-essential cmake make ca-certificates curl libcurl4-gnutls-dev
libfcgi0ldbl libfcgi-dev \  
shapelib libproj-dev libgeos-dev libpq-dev \  
libxml2 libxml2-dev libpng-dev zlib1g zlib1g-dev libjpeg-dev libfribidi0
libfribidi-dev libfreetype6 libfreetype6-dev libharfbuzz0b libharfbuzz-dev \  
-y --no-install-recommends && \  
curl http://download.osgeo.org/mapserver/mapserver-7.0.7.tar.gz | tar zx -C
/tmp && \  
mkdir /tmp/mapserver-7.0.7/build && \  
cd /tmp/mapserver-7.0.7/build && \  
cmake .. -DWITH_GDAL=1 -DWITH_CURL=1 -DWITH_CAIRO=0 -DWITH_GIF=0 && \  
make -j $(grep --count ^processor /proc/cpuinfo) && \  
make install && \  
apt-get remove --purge -y cmake make libcurl4-gnutls-dev libproj-dev libgeos-
dev libpq-dev libxml2-dev libpng-dev zlib1g-dev libjpeg-dev libfribidi-dev
libfreetype6-dev libharfbuzz-dev && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
RUN rm /etc/nginx/sites-enabled/default  
ADD etc /etc  
  
###RUN mkdir -p /usr/src  
###COPY mapfiles /usr/src/mapfiles  
  
# Set HOME dir so AWS credentials can be fetched at ~/.aws/credentials  
# https://lists.osgeo.org/pipermail/gdal-dev/2017-July/046846.html  
ENV HOME /root  
  
EXPOSE 80  
CMD sh -c "/usr/bin/supervisord"  

