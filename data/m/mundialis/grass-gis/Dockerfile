FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
  
# Workaround for resolveconf ubuntu docker issue  
# https://stackoverflow.com/questions/40877643/apt-get-install-in-
ubuntu-16-04-docker-image-etc-resolv-conf-device-or-reso  
RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-
set-selections  
  
# Install the dependencies of GRASS GIS  
RUN apt update && apt upgrade -y && \  
apt install software-properties-common -y && \  
add-apt-repository ppa:ubuntugis/ubuntugis-unstable -y && \  
apt update && apt install --no-install-recommends --no-install-suggests \  
build-essential \  
flex \  
make \  
bison \  
gcc \  
libgcc1 \  
g++ \  
python3 \  
python3-dev \  
python3-dateutil \  
python3-ply \  
python3-pip \  
libpython3-all-dev \  
libgsl0-dev \  
libncurses5-dev \  
ncurses \  
zlib1g-dev \  
gettext \  
libtiff-dev \  
libpnglite-dev \  
libcairo2 \  
libcairo2-dev \  
sqlite3 \  
libsqlite3-dev \  
libpq-dev \  
libreadline6 \  
libreadline6-dev \  
libfreetype6-dev \  
libapt-pkg-perl \  
resolvconf \  
libjasper-dev \  
ruby \  
subversion \  
libopenjp2-7-dev \  
libopenjp2-7 \  
libfftw3-bin \  
libfftw3-dev \  
libcurl4-gnutls-dev \  
libbz2-dev \  
libgnutls-dev \  
gnutls-bin \  
redis-server \  
redis-tools \  
proj-data \  
gdal-bin \  
libgdal-dev \  
libgeos-dev \  
liblas-c-dev \  
liblas-dev \  
libspatialite-dev \  
libspatialite7 \  
moreutils \  
iotop \  
atop \  
htop \  
iperf \  
attr \  
git \  
vim \  
curl \  
wget \  
unzip \  
zip \  
iputils-ping \  
python3-pandas \  
libzstd0 \  
libzstd-dev \  
bzip2 -y && \  
apt-get clean && \  
apt-get autoremove  
  
RUN echo LANG="en_US.UTF-8" > /etc/default/locale  
  
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
\--with-fftw \  
\--with-netcdf \  
\--with-bzlib \  
\--with-zstd \  
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
# Unset environmental variables to avoid laster compilation issues  
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
# for python3 usage:  
RUN apt install language-pack-en-base -y  
ENV LC_ALL "en_US.UTF-8"  
# TODO: remove compile tools (unless needed for GRASS GIS extension
installation)  

