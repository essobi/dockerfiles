FROM debian:sid  
MAINTAINER Victor M. Varela <v.varela@neartechnologies.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update \  
&& apt-get -yq install --no-install-recommends gis-devel \  
python-scipy \  
python-matplotlib \  
python-shapely \  
python-pyproj \  
python-psycopg2 \  
python-geojson \  
python-grib \  
grass-core \  
python-mapnik \  
python-saga \  
python-geopy \  
python-owslib \  
&& apt-get clean autoclean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
WORKDIR /code  
  
ENV GDAL_VERSION 1.11.2  
  
RUN BUILD_DEPS="g++ wget make python-pip python-dev" \  
&& apt-get -y install --no-install-recommends $BUILD_DEPS \  
&& wget -qO-
http://download.osgeo.org/gdal/${GDAL_VERSION}/gdal-${GDAL_VERSION}.tar.gz |
tar xz \  
&& cd /code/gdal-${GDAL_VERSION} && ./configure && make install \  
&& pip install GDAL \  
&& apt-get -y remove --purge $BUILD_DEPS \  
&& apt-get -y autoremove --purge \  
&& rm -rf /var/lib/{apt,dpkg,cache,log} \  
&& rm -rf /code/*  
  
ENV BUFR_VERSION 000403  
  
RUN BUILD_DEPS="wget gfortran make python-setuptools python-dev" \  
&& apt-get -y install --no-install-recommends ${BUILD_DEPS} \  
&& wget -qO- --no-check-certificate https://github.com/mraspaud/python-
bufr/archive/master.tar.gz | tar xz \  
&& wget -qO- --no-check-certificate
https://software.ecmwf.int/wiki/download/attachments/35752466/bufrdc_${BUFR_VERSION}.tar.gz
| tar xz \  
&& cd /code/bufrdc_${BUFR_VERSION} && sed -i "s/PROFILE=/PROFILE=-fPIC/"
config/config.linux_gfortranR64A64.in \  
&& (echo y; echo y; echo /usr/lib) | sh build_library && sh install \  
&& cd /code/python-bufr-master/bufr && python setup.py build_ext -lbufrR64 \  
&& python setup.py install \  
&& apt-get -y remove --purge ${BUILD_DEPS} \  
&& apt-get -y autoremove --purge \  
&& rm -rf /var/lib/{apt,dpkg,cache,log} \  
&& rm -rf /code/*  
  
RUN BUILD_DEPS="wget gfortran make gcc" \  
&& apt-get -y install --no-install-recommends ${BUILD_DEPS} \  
&& wget -qO- ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz | tar xz \  
&& cd grib2 && CC=gcc FC=gfortran make && cp wgrib2/wgrib2 /usr/local/bin \  
&& apt-get -y remove --purge ${BUILD_DEPS} \  
&& apt-get -y autoremove --purge \  
&& rm -rf /var/lib/{apt,dpkg,cache,log} \  
&& rm -rf /code/*  
  

