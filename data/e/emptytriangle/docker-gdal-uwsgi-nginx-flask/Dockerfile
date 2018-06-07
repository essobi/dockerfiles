FROM tiangolo/uwsgi-nginx-flask:flask  
  
# Maintainer of the original UWSGI-NGINX-FLASK image:
https://github.com/tiangolo/uwsgi-nginx-flask-docker  
MAINTAINER Sebastian Ramirez <tiangolo@gmail.com>  
# Maintainer of the original GDAL image:
https://hub.docker.com/r/klokantech/gdal/  
# https://gist.github.com/klokan/bfd4a07e8072ffae4bb6  
MAINTAINER Klokantech  
# Maintainer of the merged image w/ additional FGDB support  
MAINTAINER Keith Moss <keithamoss@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update \  
&& apt-get -qq -y --no-install-recommends install \  
autoconf \  
automake \  
build-essential \  
curl \  
libcurl3-gnutls-dev \  
libepsilon-dev \  
libexpat-dev \  
libfreexl-dev \  
libgeos-dev \  
libgif-dev \  
libhdf4-alt-dev \  
libhdf5-serial-dev \  
libjpeg-dev \  
liblcms2-dev \  
liblzma-dev \  
libnetcdf-dev \  
libpcre3-dev \  
libpng12-dev \  
libpodofo-dev \  
libpoppler-dev \  
libproj-dev \  
libspatialite-dev \  
libsqlite3-dev \  
libtbb2 \  
libwebp-dev \  
libxerces-c-dev \  
libxml2-dev \  
netcdf-bin \  
poppler-utils \  
python-dev \  
unixodbc-dev \  
unzip  
  
# Install GDAL  
ENV GDAL_VERSION 2.1.1  
  
RUN mkdir -p /usr/local/src \  
&& curl -s
http://download.osgeo.org/gdal/$GDAL_VERSION/gdal-$GDAL_VERSION.tar.gz \  
| tar xz -C /usr/local/src  
WORKDIR /usr/local/src/gdal-$GDAL_VERSION  
  
RUN ./configure \  
\--prefix=/usr/local \  
\--without-libtool \  
\--with-epsilon \  
\--with-libkml \  
\--with-liblzma \  
\--with-podofo \  
\--with-poppler \  
\--with-python \  
\--with-spatialite \  
\--with-threads \  
\--with-webp \  
&& make install \  
&& ldconfig  
  
# Externally accessible data is by default put in /data  
# WORKDIR /data  
# VOLUME ["/data"]  
# Execute the gdal utilities as nobody, not root  
# USER nobody  
# Output version and capabilities by default.  
# CMD gdalinfo --version && gdalinfo --formats && ogrinfo --formats  
# Add app configuration to Nginx  
COPY nginx.conf /etc/nginx/conf.d/  
  
# Copy sample app  
COPY ./app /app  

