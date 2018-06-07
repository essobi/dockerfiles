FROM debian:jessie  
  
ENV MAPCACHE_VERSION="1.4.1" \  
MAPCACHE_CONFIG_FILE="/usr/local/etc/mapcache.xml" \  
MAPCACHE_FASTCGI_PORT=9005 \  
MAPCACHE_FASTCGI_CHILDREN=1 \  
MAPCACHE_FASTCGI_ADDRESS="0.0.0.0"  
  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget \  
cmake \  
spawn-fcgi \  
multiwatch \  
build-essential \  
libapr1-dev \  
libaprutil1-dev \  
libpng12-dev \  
libjpeg62-turbo-dev \  
libcurl4-openssl-dev \  
libpcre3-dev \  
libpixman-1-dev \  
libfcgi-dev \  
libgdal1-dev \  
libgeos-dev \  
libsqlite3-dev \  
libgeotiff-dev \  
libtiff5-dev  
RUN wget -O /tmp/mapcache-${MAPCACHE_VERSION}.tar.gz
http://download.osgeo.org/mapserver/mapcache-${MAPCACHE_VERSION}.tar.gz \  
&& cd /tmp \  
&& tar xvfz /tmp/mapcache-${MAPCACHE_VERSION}.tar.gz \  
&& mkdir /tmp/mapcache-${MAPCACHE_VERSION}/build \  
&& cd /tmp/mapcache-${MAPCACHE_VERSION}/build \  
&& cmake .. \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
-DCMAKE_BUILD_TYPE=Release \  
-DWITH_APACHE=0 \  
-DWITH_PIXMAN=ON \  
-DWITH_SQLITE=ON \  
-DWITH_TIFF=ON \  
-DWITH_GEOTIFF=ON \  
-DWITH_PCRE=ON \  
-DWITH_GEOS=ON \  
-DWITH_OGR=ON \  
-DWITH_CGI=ON \  
-DWITH_FCGI=ON \  
-DWITH_VERSION_STRING=ON \  
&& make -j$(nproc) \  
&& make install \  
&& cd /tmp \  
&& rm -rf /tmp/mapcache-${MAPCACHE_VERSION} \  
&& ldconfig  
  
CMD /usr/bin/spawn-fcgi -n -a ${MAPCACHE_FASTCGI_ADDRESS} -p
${MAPCACHE_FASTCGI_PORT} -- /usr/bin/multiwatch -f
${MAPCACHE_FASTCGI_CHILDREN} -- /usr/local/bin/mapcache.fcgi  

