FROM centos:7  
  
ENV BOOST_INSTALL_VERSION=1.60.0 \  
MAPNIK_INSTALL_VERSION=3.0.12 \  
PATH=/usr/pgsql-9.5/bin:$PATH \  
CC=/usr/bin/clang \  
CXX=/usr/bin/clang++ \  
LD_LIBRARY_PATH=/usr/local/lib  
  
RUN yum -y update && \  
yum -y install epel-release && \  
yum -y install
https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-
centos95-9.5-2.noarch.rpm && \  
yum -y install \  
bzip2 \  
bzip2-devel \  
cairo-devel \  
clang \  
file \  
gcc-c++ \  
gdal-devel \  
git \  
harfbuzz-devel \  
libjpeg-turbo-devel \  
libtiff-devel \  
libwebp-devel \  
make \  
postgresql95-devel \  
postgis2_95-devel \  
proj-devel \  
proj-epsg \  
python-devel \  
sqlite-devel \  
tar \  
wget \  
which \  
&& \  
yum clean all && \  
cd /opt && \  
export BOOST_DOWNLOAD_VERSION=$(echo $BOOST_INSTALL_VERSION | tr . _) && \  
wget -nv
http://downloads.sourceforge.net/project/boost/boost/${BOOST_INSTALL_VERSION}/boost_${BOOST_DOWNLOAD_VERSION}.tar.bz2
&& \  
export BOOST_DOWNLOAD_VERSION=$(echo $BOOST_INSTALL_VERSION | tr . _) && \  
tar -xjf boost_${BOOST_DOWNLOAD_VERSION}.tar.bz2 && \  
cd /opt/boost_${BOOST_DOWNLOAD_VERSION} && \  
./bootstrap.sh --with-toolset=clang && \  
./b2 install toolset=clang -d0 && \  
cd /opt && \  
git clone -b v${MAPNIK_INSTALL_VERSION} --single-branch --recursive
https://github.com/mapnik/mapnik.git mapnik-${MAPNIK_INSTALL_VERSION} && \  
cd /opt/mapnik-${MAPNIK_INSTALL_VERSION} && \  
./configure CXX=clang++ CC=clang && \  
make --silent && \  
make install

