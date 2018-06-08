FROM ubuntu:xenial  
LABEL maintainer "Cheewai Lai <clai@csir.co.za>"  
  
ARG GOSU_VERSION=1.10  
ARG
GOSU_DOWNLOAD_URL="https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-
amd64"  
ARG S6_OVERLAY_VERSION=v1.20.0.0  
ARG DEBIAN_FRONTEND=noninteractive  
ARG DOCKERIZE_VERSION=v0.5.0  
# For PyHDF compilation  
ARG PYHDF_VERSION=0.9.0  
ARG PYHDF_URL=http://hdfeos.org/software/pyhdf/pyhdf-${PYHDF_VERSION}.tar.gz  
ARG INCLUDE_DIRS=/usr/include/hdf  
ARG NOSZIP=1  
# For libspatialindex, rtree  
ARG SPATIALINDEX_VER=1.8.5  
#2017-09-27 ARG LIBGEOS_VER=3.4.2  
ARG LIBGEOS_VER=3.5.0  
# For sklearn.cluster: python-numpy libatlas-dev libatlas3gf-base  
# For scipy: liblapack3gf liblapack-dev gfortran  
# For Python script to interact with Postgis database: python-psycopg2
libgeos-3.4.2 libgeos-dev  
RUN sed 's/main$/main universe multiverse/' -i /etc/apt/sources.list \  
&& set -x \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y curl software-properties-common wget unzip build-
essential git python python-dev python-setuptools bzip2 jq \  
&& curl -o gosu -fsSL "$GOSU_DOWNLOAD_URL" > gosu-amd64 \  
&& mv gosu /usr/bin/gosu \  
&& chmod +x /usr/bin/gosu \  
&& curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar xfz - -C / \  
&& curl -k -fsSL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xfz - -C /usr/bin \  
&& easy_install pip \  
&& pip install --upgrade pip \  
&& apt-get install -y python-numpy python-tables liblapack3 liblapack-dev
gfortran python-psycopg2 libgeos-${LIBGEOS_VER} libgeos-dev python-yaml
python-gdal libgdal1i gdal-bin \  
&& pip install pyproj \  
&& pip install pytest \  
&& pip install python-logstash \  
&& pip install subprocess32 \  
&& pip install rethinkdb \  
&& pip install shapely \  
&& pip install pika \  
&& apt-get -y install libgrib-api-dev \  
&& pip install pygrib \  
&& ldconfig  
  
RUN curl -o /tmp/spatialindex.tgz
http://download.osgeo.org/libspatialindex/spatialindex-
src-${SPATIALINDEX_VER}.tar.gz \  
&& tar -C /tmp -zxf /tmp/spatialindex.tgz \  
&& cd /tmp/spatialindex-src-${SPATIALINDEX_VER} \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& pip install --upgrade rtree \  
&& pip install dateutils \  
&& pip install blinker raven --upgrade \  
&& apt-get -y install libhdf4-dev \  
&& curl -o /tmp/pyhdf.tgz -fsSL $PYHDF_URL \  
&& cd /tmp \  
&& tar zxvf pyhdf.tgz \  
&& cd /tmp/pyhdf-${PYHDF_VERSION} \  
&& python setup.py install \  
&& apt-get -y remove --purge software-properties-common build-essential git
python-dev \  
&& apt-get -y autoremove \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 755 /docker-entrypoint.sh \  
&& chown root.root /docker-entrypoint.sh  

