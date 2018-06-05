FROM danielquinn/django  
  
COPY requirements.txt /  
  
# Install dependencies: first from apk, then from pip, then clean out bits we  
# only needed for installation.  
RUN \  
apk add --update --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
\  
gdal-dev geos-dev proj4-dev sqlite-dev \  
gdal geos proj4 \  
git gcc g++ coreutils make \  
libjpeg-turbo-dev giflib-dev \  
tzdata && \  
\  
pip3 install --requirement requirements.txt && \  
\  
wget http://www.gaia-gis.it/gaia-sins/libspatialite-4.3.0a.tar.gz && \  
tar xzf libspatialite-4.3.0a.tar.gz && \  
rm libspatialite-4.3.0a.tar.gz && \  
cd libspatialite-4.3.0a && \  
CFLAGS="-DSQLITE_ENABLE_RTREE=1" ./configure --disable-freexl --disable-
libxml2 && \  
make -j$(nproc) && \  
make install && \  
cd && rm -rf /usr/src/libspatialite-4.3.0a && \  
\  
\  
apk del gcc g++ coreutils make && \  
rm /var/cache/apk/*  

