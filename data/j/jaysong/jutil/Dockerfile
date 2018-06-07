FROM java:8  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
gdb \  
osmctools \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
##########################################################################################  
ARG
MAT_SHA512=212713dff859ff8f2b1cb898584ff0a1c16abf4ef0264ef5cc410416957ac5282bb02f2e4ecd46dbb0e7beb3fbfce229588f1231cb88b725af5ca62b22c23b3c  
ARG
MAT_URL=http://mirror.csclub.uwaterloo.ca/eclipse/mat/1.6/rcp/MemoryAnalyzer-1.6.0.20160531-linux.gtk.x86_64.zip  
ADD $MAT_URL /usr/bin/mat.zip  
  
WORKDIR /usr/bin  
RUN echo "$MAT_SHA512 mat.zip" | sha512sum -c - && \  
unzip mat.zip && \  
ln -s mat/MemoryAnalyzer MemoryAnalyzer && \  
rm mat.zip  
  
##########################################################################################  
ARG OSMOSIS_URL=http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-
latest.tgz  
ADD $OSMOSIS_URL /usr/bin/  
  
WORKDIR /usr/bin  
RUN mkdir osmosis-latest && \  
tar xvzf osmosis-latest.tgz -C osmosis-latest && \  
chmod a+x osmosis-latest/bin/osmosis && \  
ln -s osmosis-latest/bin/osmosis osmosis && \  
rm osmosis-latest.tgz  
  
##########################################################################################  
ARG GEOS_DIST=geos-3.6.1  
ARG GEOS_URL=http://download.osgeo.org/geos/${GEOS_DIST}.tar.bz2  
ADD $GEOS_URL /tmp/  
  
WORKDIR /tmp  
RUN tar xvjf ${GEOS_DIST}.tar.bz2 && \  
cd ${GEOS_DIST} && \  
./configure && \  
make && \  
make install && \  
ldconfig && \  
cd /tmp && \  
rm -fr ${GEOS_DIST}*  
  
##########################################################################################  
ARG PROJ_DIST=proj-4.9.3  
ARG PROJ_URL=http://download.osgeo.org/proj/${PROJ_DIST}.tar.gz  
ADD $PROJ_URL /tmp/  
  
WORKDIR /tmp  
RUN tar xvzf ${PROJ_DIST}.tar.gz && \  
cd ${PROJ_DIST} && \  
./configure && \  
make && \  
make install && \  
ldconfig && \  
cd /tmp && \  
rm -fr ${PROJ_DIST}*  
  
##########################################################################################  
ARG GDAL_DIST=gdal-2.1.3  
ARG GDAL_URL=http://download.osgeo.org/gdal/2.1.3/${GDAL_DIST}.tar.gz  
ADD $GDAL_URL /tmp/  
  
WORKDIR /tmp  
RUN tar xvzf ${GDAL_DIST}.tar.gz && \  
cd ${GDAL_DIST} && \  
./configure && \  
make && \  
make install && \  
ldconfig && \  
cd /tmp && \  
rm -fr ${GDAL_DIST}*  
  
##########################################################################################  
COPY ./util/* /_util/  
  
VOLUME ["/app", "/data"]  
WORKDIR /app  
  
CMD ["/bin/bash"]  

