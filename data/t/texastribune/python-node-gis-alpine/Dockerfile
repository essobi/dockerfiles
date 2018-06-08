FROM python:3.5-alpine  
  
# install all the dependencies for GeoDjango and Node.js asset pipeline  
RUN set -ex \  
&& apk add --no-cache \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \  
autoconf \  
automake \  
gcc \  
gdal-dev \  
geos \  
make \  
musl-dev \  
nasm \  
nodejs \  
postgresql-dev \  
proj4  
  
# link geo libraries so Django can find them  
RUN ln -s /usr/lib/libgeos_c.so.1 /usr/local/lib/libgeos_c.so  
RUN ln -s /usr/lib/libgdal.so.20.1.0 /usr/local/lib/libgdal.so

