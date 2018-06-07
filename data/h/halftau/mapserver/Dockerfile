FROM alpine:3.4  
  
MAINTAINER Pablo Perich <pablo.perich@halftau.com>  
  
RUN apk add \  
libcurl \  
fcgi \  
spawn-fcgi \  
cairo \  
fribidi \  
libxml2 \  
libxslt \  
librsvg \  
boost \  
jpeg \  
giflib \  
libpq \  
\--update && \  
  
apk add \  
gdal \  
geos \  
proj4 \  
\--update --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ && \  
  
apk add \  
g++ \  
make \  
cmake \  
wget \  
curl-dev \  
fcgi-dev \  
cairo-dev \  
fribidi-dev \  
libxml2-dev \  
libxslt-dev \  
librsvg-dev \  
boost-dev \  
jpeg-dev \  
giflib-dev \  
postgresql-dev \  
\--virtual devpacks && \  
  
apk add \  
gdal-dev \  
geos-dev \  
proj4-dev \  
\--virtual devpacks \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ && \  
  
cd /tmp && wget
https://libopenraw.freedesktop.org/download/exempi-2.3.0.tar.bz2 && \  
tar xjf exempi-2.3.0.tar.bz2 && \  
cd exempi-2.3.0 && \  
./configure && \  
make && \  
make install && \  
cd /tmp && \  
rm -rf * && \  
  
mkdir -p /usr/local/src && \  
cd /usr/local/src && \  
wget http://download.osgeo.org/mapserver/mapserver-7.0.1.tar.gz && \  
tar -xzvf mapserver-7.0.1.tar.gz && \  
mkdir /usr/local/src/mapserver-7.0.1/build && \  
cd /usr/local/src/mapserver-7.0.1/build && \  
cmake ../ -DWITH_THREAD_SAFETY=1 \  
-DWITH_PROJ=1 \   
-DWITH_KML=1 \   
-DWITH_SOS=1 \   
-DWITH_WMS=1 \   
-DWITH_FRIBIDI=1 \   
-DWITH_HARFBUZZ=1 \   
-DWITH_ICONV=1 \   
-DWITH_CAIRO=1 \   
-DWITH_RSVG=1 \   
-DWITH_MYSQL=0 \   
-DWITH_GEOS=1 \   
-DWITH_POSTGIS=1 \   
-DWITH_GDAL=1 \   
-DWITH_OGR=1 \   
-DWITH_CURL=1 \   
-DWITH_CLIENT_WMS=1 \   
-DWITH_CLIENT_WFS=1 \   
-DWITH_WFS=1 \   
-DWITH_WCS=1 \   
-DWITH_LIBXML2=1 \   
-DWITH_GIF=1 \   
-DWITH_EXEMPI=1 \   
-DWITH_XMLMAPFILE=1 \   
-DWITH_FCGI=1 && \   
make && \  
make install && \  
cd /usr/local/src && \  
rm -rf * && \  
  
apk del devpacks --purge  
  
  
WORKDIR /maps  
  
EXPOSE 9999  
  
ENV MS_ERRORFILE=stderr  
  
USER nobody  
#CMD /usr/bin/spawn-fcgi -n -f /usr/local/bin/mapserv -d /maps -u nobody -g
nobody -p 9999 -P /var/run/fastcgi-mapsrv.pid  
#CMD [ "/usr/bin/spawn-fcgi", "-n", "-f /usr/local/bin/mapserv", "-d/maps",
"-unobody", "-gnobody", "-p 9999", "-P/var/run/fastcgi-mapsrv.pid" ]  
CMD [ "/usr/bin/spawn-fcgi", "-n", "-d/maps", "-unobody", "-gnobody", "-p
9999", "/usr/local/bin/mapserv" ]  

