FROM python:3.6-alpine  
  
LABEL org.label-schema.name = "gdal-python-alpine"  
LABEL org.label-schema.description = "Alpine-based image with Python and
GDAL/OGR, compiled with selected additional drivers."  
LABEL org.label-schema.vcs-url = "https://github.com/petr-k/gdal-python-
alpine"  
LABEL org.label-schema.vendor = "Petr Krebs"  
  
ARG GDAL_VERSION=v2.2.4  
ARG LIBKML_VERSION=1.3.0  
  
RUN \  
apk update && \  
apk add --virtual build-dependencies \  
# to reach GitHub's https  
openssl ca-certificates \  
build-base cmake musl-dev linux-headers \  
# for libkml compilation  
zlib-dev minizip-dev expat-dev uriparser-dev boost-dev && \  
apk add \  
# libkml runtime  
zlib minizip expat uriparser boost && \  
update-ca-certificates && \  
mkdir /build && cd /build && \  
apk --update add tar && \  
# libkml  
wget -O libkml.tar.gz
"https://github.com/libkml/libkml/archive/${LIBKML_VERSION}.tar.gz" && \  
tar --extract --file libkml.tar.gz && \  
cd libkml-${LIBKML_VERSION} && mkdir build && cd build && cmake .. && make &&
make install && cd ../.. && \  
# gdal  
wget -O gdal.tar.gz
"https://github.com/OSGeo/gdal/archive/${GDAL_VERSION}.tar.gz" && \  
tar --extract --file gdal.tar.gz --strip-components 1 && \  
cd gdal && \  
./configure --prefix=/usr \  
\--with-libkml \  
\--without-bsb \  
\--without-dwgdirect \  
\--without-ecw \  
\--without-fme \  
\--without-gnm \  
\--without-grass \  
\--without-grib \  
\--without-hdf4 \  
\--without-hdf5 \  
\--without-idb \  
\--without-ingress \  
\--without-jasper \  
\--without-mrf \  
\--without-mrsid \  
\--without-netcdf \  
\--without-pcdisk \  
\--without-pcraster \  
\--without-webp \  
&& make && make install && \  
# gdal python bindings  
pip install gdal --no-cache-dir && \  
# cleanup  
apk del build-dependencies && \  
cd / && \  
rm -rf build && \  
rm -rf /var/cache/apk/* && \  
rm -rf /usr/lib/python2.7  

