FROM ubuntu:xenial  
LABEL maintainer "Cheewai Lai <clai@csir.co.za>"  
  
ARG SUEXEC_VER=0.2  
ARG DOCKERIZE_VERSION=v0.5.0  
# For libspatialindex, rtree  
ARG SPATIALINDEX_VER=1.8.5  
  
ARG LIBGEOS_VER=3.5.0  
# For HDF5 LPC-Rice filter to process Derick's cube  
ARG LPCRICE_VER=0.2  
# For sklearn.cluster: python-numpy libatlas-dev libatlas3gf-base  
# For scipy: liblapack3gf liblapack-dev gfortran  
# For Python script to interact with Postgis database: python-psycopg2
libgeos-3.4.2 libgeos-dev  
ARG DEBIAN_FRONTEND=noninteractive  
RUN sed 's/main$/main universe multiverse/' -i /etc/apt/sources.list \  
&& set -x \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y curl software-properties-common wget unzip build-
essential git python python-dev python-setuptools bzip2 jq \  
&& curl -k -fsSL -o /tmp/suexec.tgz "https://github.com/ncopa/su-
exec/archive/v${SUEXEC_VER}.tar.gz" \  
&& cd /tmp \  
&& tar xvf suexec.tgz \  
&& cd "/tmp/su-exec-${SUEXEC_VER}" \  
&& make \  
&& cp -af su-exec /usr/bin/ \  
&& curl -k -fsSL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xfz - -C /usr/bin \  
&& easy_install pip \  
&& pip install --upgrade pip \  
&& apt-get install -y python-numpy python-tables liblapack3 liblapack-dev
gfortran python-psycopg2 libgeos-${LIBGEOS_VER} libgeos-dev python-yaml
python-gdal libgdal1i gdal-bin python-h5py hdf5-tools libhdf5-dev logrotate \  
&& pip install pyproj \  
&& pip install pytest \  
&& pip install subprocess32 \  
&& pip install rethinkdb \  
&& curl -o /tmp/spatialindex.tgz
http://download.osgeo.org/libspatialindex/spatialindex-
src-${SPATIALINDEX_VER}.tar.gz \  
&& tar -C /tmp -zxf /tmp/spatialindex.tgz \  
&& cd /tmp/spatialindex-src-${SPATIALINDEX_VER} \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& pip install dateutils \  
&& pip install blinker raven --upgrade \  
&& wget -O /tmp/lpcrice-hdf-filter.zip
https://sourceforge.net/projects/lpcrice/files/lpcrice-hdf-
filter-v${LPCRICE_VER}.zip/download && unzip /tmp/lpcrice-hdf-filter.zip -d
/tmp && cd /tmp/lpcrice-hdf-filter-v${LPCRICE_VER} && chmod -R 777 . \  
&& sed -i -e '/^INCLUDES/ s|$| -I/usr/include/hdf5/serial/|' -e '/ -lhdf5/
s|$| -L/usr/lib/x86_64-linux-gnu/hdf5/serial|' Makefile \  
&& make && mkdir -p /usr/local/hdf5/lib/plugin && cp -a libh5rice.so*
/usr/local/hdf5/lib/plugin \  
&& apt-get -y install cmake \  
&& cd /tmp && git clone https://github.com/Blosc/c-blosc.git \  
&& mkdir c-blosc/build \  
&& cd c-blosc/build \  
&& cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \  
&& cmake --build . \  
&& cmake --build . --target install \  
&& ldconfig \  
&& cd /tmp && git clone https://github.com/Blosc/hdf5-blosc.git \  
&& mkdir hdf5-blosc/build \  
&& cd hdf5-blosc/build \  
&& cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \  
&& cmake --build . \  
&& ctest \  
&& cmake --build . --target install \  
&& for f in /usr/local/lib/libblosc* ; do \  
test -L $f || ln -s $f /usr/local/hdf5/lib/plugin/ ; \  
done \  
&& ldconfig \  
&& apt-get -y remove --purge software-properties-common build-essential git
python-dev gfortran cmake \  
&& apt-get -y autoremove \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  

