FROM alpine:latest  
MAINTAINER Kostas Andreadis <kandread@jpl.nasa.gov>  
  
ENV POSTGIS_VERSION 2.4.3  
ENV NETCDF_VERSION 4.6.1  
RUN mkdir -p /etc/apk  
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk add --no-cache --virtual .build-deps automake autoconf gcc g++ make
python-dev gfortran musl-dev libxslt-dev openblas-dev postgresql-dev hdf5-dev
gdal-dev curl-dev wget m4 cython-dev git json-c-dev libtool libxml2-dev
proj4-dev geos-dev  
RUN apk add --no-cache python py-pip freetype libgfortran libgcc libpng
libstdc++ musl openblas cython curl wine gdal hdf5 postgresql bash json-c geos
proj4  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
RUN wget https://github.com/Unidata/netcdf-c/archive/v$NETCDF_VERSION.tar.gz
&& tar xf v$NETCDF_VERSION.tar.gz && cd netcdf-c-$NETCDF_VERSION &&
./configure --prefix=/usr --disable-dependency-tracking && make -j2 && make
install  
RUN wget -O postgis.tar.gz
"https://github.com/postgis/postgis/archive/$POSTGIS_VERSION.tar.gz" && mkdir
-p /usr/src/postgis && tar --extract --file postgis.tar.gz --directory
/usr/src/postgis --strip-components 1 && rm postgis.tar.gz  
RUN cd /usr/src/postgis && ./autogen.sh && ./configure && make && make install
&& cd / && rm -rf /usr/src/postgis  
ADD requirements.txt /  
RUN pip install --no-cache-dir -r /requirements.txt  
  
RUN addgroup -g 888 rheas  
RUN adduser -D -u 888 -G rheas rheas  
  
RUN git clone https://github.com/nasa/RHEAS.git /rheas  
RUN chown -R rheas:rheas /rheas  
WORKDIR /rheas  
COPY buildout.cfg .  
ENV USER rheas  
ENV EARTHDATA_USER nasarheas  
ENV EARTHDATA_PASSWORD rheas@Earthdata1  
RUN python bootstrap.py  
RUN ./bin/buildout  
RUN apk del .build-deps && rm -rf /root/.cache  

