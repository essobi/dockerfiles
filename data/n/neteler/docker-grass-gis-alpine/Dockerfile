FROM alpine:edge  
  
WORKDIR /tmp  
  
RUN \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories; \  
echo "@edgecommunity http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories; \  
apk update  
  
# Install the build dependencies of GRASS GIS  
RUN apk add --no-cache --virtual .build-deps \  
build-base abuild binutils gcc \  
gdal-dev \  
geos-dev \  
libgeotiff-dev \  
libxml2-dev \  
python-dev \  
py-numpy-dev \  
jsoncpp-dev \  
sqlite \  
sqlite-dev \  
sqlite-libs \  
hdf5-dev \  
proj4-dev \  
laszip-dev \  
laz-perf-dev \  
curl-dev \  
unzip \  
ca-certificates \  
wget \  
bison \  
libpng \  
libpng-dev \  
cairo \  
cairo-dev \  
gettext \  
tiff-dev \  
jasper-dev \  
subversion \  
openjpeg \  
openjpeg-dev \  
bzip2 \  
bzip2-dev \  
gnutls \  
gnutls-dev \  
gnutls-utils \  
proj4 \  
proj4-dev \  
git \  
python2 \  
py2-dateutil \  
py2-pip \  
flex  
  
RUN apk add --no-cache --virtual .build-deps \  
eigen-dev@edgecommunity  
  
RUN apk add --no-cache \  
bash \  
ncurses \  
gdal \  
geos \  
laz-perf \  
libgeotiff \  
libxml2 \  
python2 \  
py2-numpy \  
jsoncpp \  
hdf5 \  
proj4 \  
sqlite \  
laszip \  
zip \  
bzip2 \  
redis \  
moreutils \  
iotop \  
atop \  
htop \  
iperf \  
attr \  
vim \  
curl \  
iputils  
  
WORKDIR /src  
  
# install the latest projection library for GRASS GIS  
RUN wget http://download.osgeo.org/proj/proj-4.9.3.tar.gz && \  
tar xzvf proj-4.9.3.tar.gz && cd /src/proj-4.9.3/ && \  
wget http://download.osgeo.org/proj/proj-datumgrid-1.6.zip  
WORKDIR /src/proj-4.9.3  
RUN cd nad && \  
unzip ../proj-datumgrid-1.6.zip && cd ..  
RUN /src/proj-4.9.3/configure && make -j4 && make install  
  
# Checkout and install GRASS GIS  
WORKDIR /src  
  
## TODO change trunk to release_branch74  
#RUN svn checkout https://svn.osgeo.org/grass/grass/trunk grass_trunk  
RUN wget
https://grass.osgeo.org/grass75/source/snapshot/grass-7.5.svn_src_snapshot_latest.tar.gz  
# unpack source code package and remove tarball archive:  
RUN tar xvfz grass-7.5.svn_src_snapshot_latest.tar.gz  
RUN rm -f grass-7.5.svn_src_snapshot_latest.tar.gz  
  
# rename source code directory  
RUN mv grass-7.5.svn_src_snapshot_20??_??_?? grass_trunk  
  
# update snapshot once more to grab latest updates and fixes:  
WORKDIR /src/grass_trunk  
RUN svn update  
  
# Set environmental variables for GRASS GIS compilation, without debug symbols  
ENV INTEL "-march=native -std=gnu99 -fexceptions -fstack-protector -m64"  
ENV MYCFLAGS "-Wall -fno-fast-math -fno-common $INTEL"  
ENV MYLDFLAGS "-s -Wl,--no-undefined"  
# CXX stuff:  
ENV LD_LIBRARY_PATH "/usr/local/lib"  
ENV LDFLAGS "$MYLDFLAGS"  
ENV CFLAGS "$MYCFLAGS"  
ENV CXXFLAGS "$MYCXXFLAGS"  
# Configure compile and install  
RUN /src/grass_trunk/configure \  
\--with-cxx \  
\--enable-largefile \  
\--with-proj=/usr/local/lib \  
\--with-proj-share=/usr/local/share/proj \  
\--with-gdal \  
\--with-python \  
\--with-geos \  
\--with-sqlite \  
\--with-cairo --with-cairo-ldflags=-lfontconfig \  
\--with-bzlib \  
\--without-fftw \  
\--without-netcdf \  
\--without-zstd \  
\--without-postgres \  
\--without-freetype \  
\--without-openmp \  
\--without-opengl \  
\--without-nls \  
\--without-mysql \  
\--without-odbc \  
\--without-openmp \  
\--without-ffmpeg \  
\--prefix=/usr/local && make -j4 && make install  
  
# TODO Install the module to render several maps at once  
# Unset environmental variables to avoid later compilation issues  
ENV INTEL ""  
ENV MYCFLAGS ""  
ENV MYLDFLAGS ""  
ENV MYCXXFLAGS ""  
ENV LD_LIBRARY_PATH ""  
ENV LDFLAGS ""  
ENV CFLAGS ""  
ENV CXXFLAGS ""  
# Download and unpack the sample data  
WORKDIR /grassdb  
VOLUME /grassdb  
  
# Clean up the compiled files  
RUN rm -rf /src/*  
  
# GRASS GIS specific  
ENV GRASS_SKIP_MAPSET_OWNER_CHECK 1  
ENV LC_ALL "en_US.UTF-8"  
RUN apk del .build-deps  

