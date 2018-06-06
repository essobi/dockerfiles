FROM mdillon/postgis  
MAINTAINER Jorge Martinez <jorge@terranodo.io>  
  
ADD init.sh /docker-entrypoint-initdb.d/  
  
  
RUN apt-get update && \  
apt-get install -y git \  
cmake \  
libxml2-dev \  
autoconf \  
g++ \  
zlib1g-dev \  
libpq-dev \  
postgresql-server-dev-10 \  
libgdal-dev \  
postgresql-plpython-10  
# Compile PointCloud  
RUN git clone https://github.com/pgpointcloud/pointcloud.git  
RUN cd pointcloud && ./autogen.sh && ./configure && make -j3 && make install  
  
# cleanup  
RUN rm -Rf pointcloud  
  
# Compile PDAL  
RUN git clone https://github.com/PDAL/PDAL.git pdal  
RUN mkdir PDAL-build && \  
cd PDAL-build && \  
cmake ../pdal && \  
make -j3 && \  
make install  
# cleanup  
RUN rm -Rf pdal && rm -Rf PDAL-build  
  
  
# all -dev packages  
RUN apt-get remove -y --purge autotools-dev \  
libgeos-dev \  
libgif-dev \  
libgl1-mesa-dev \  
libglu1-mesa-dev \  
libgpg-error-dev \  
libhdf4-alt-dev \  
libhdf5-dev \  
libicu-dev \  
libidn11-dev \  
libjbig-dev \  
libjpeg-dev \  
libkrb5-dev \  
libldap2-dev \  
libltdl-dev \  
liblzma-dev \  
libnetcdf-dev \  
libopenthreads-dev \  
libp11-kit-dev \  
libpthread-stubs0-dev \  
librtmp-dev \  
libspatialite-dev \  
libsqlite3-dev \  
libssl-dev \  
libtasn1-6-dev \  
libtiff5-dev \  
libwebp-dev \  
libx11-dev \  
libx11-xcb-dev \  
libxau-dev \  
libxcb1-dev \  
libxcb-dri2-0-dev \  
libxcb-dri3-dev \  
libxcb-glx0-dev \  
libxcb-present-dev \  
libxcb-randr0-dev \  
libxcb-render0-dev \  
libxcb-shape0-dev \  
libxcb-sync-dev \  
libxcb-xfixes0-dev \  
libxdamage-dev \  
libxdmcp-dev \  
libxerces-c-dev \  
libxext-dev \  
libxfixes-dev \  
libxshmfence-dev \  
libxxf86vm-dev \  
linux-libc-dev \  
manpages-dev \  
mesa-common-dev \  
libgcrypt11-dev \  
unixodbc-dev \  
uuid-dev \  
x11proto-core-dev \  
x11proto-damage-dev \  
x11proto-dri2-dev \  
x11proto-fixes-dev \  
x11proto-gl-dev \  
x11proto-input-dev \  
x11proto-kb-dev \  
x11proto-xext-dev \  
x11proto-xf86vidmode-dev \  
xtrans-dev \  
zlib1g-dev  
  
# installed packages  
RUN apt-get remove -y --purge autoconf \  
build-essential \  
cmake \  
docbook-mathml \  
docbook-xsl \  
libboost-dev \  
libboost-filesystem-dev \  
libboost-timer-dev \  
libcgal-dev \  
libcunit1-dev \  
libgdal-dev \  
libgeos++-dev \  
libgeotiff-dev \  
libgmp-dev \  
libjson-c-dev \  
liblas-dev \  
libmpfr-dev \  
libopenscenegraph-dev \  
libpq-dev \  
libproj-dev \  
libxml2-dev \  
postgresql-server-dev-10 \  
xsltproc \  
git \  
build-essential \  
wget  
  
# additional compilation packages  
RUN apt-get remove -y --purge automake m4 make  

