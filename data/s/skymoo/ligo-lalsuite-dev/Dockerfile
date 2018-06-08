FROM debian:buster  
  
LABEL name="LALSuite Development - Debian Buster" \  
maintainer="Adam Mercer <adam.mercer@ligo.org>" \  
date="20180606" \  
support="Best Effort"  
# ensure non-interactive debian installation  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# install apt-utils, apt-transport-https, and dirmngr  
RUN apt-get update && apt-get --assume-yes install apt-utils \  
apt-transport-https \  
ca-certificates \  
dirmngr  
  
# add upstream git-lfs repository  
# FIXME: switch to buster packages when they are available  
RUN echo "deb https://packagecloud.io/github/git-lfs/debian stretch main" >
/etc/apt/sources.list.d/git-lfs.list  
RUN apt-key adv --keyserver pgp.mit.edu --recv-key
418A7F2FB0E1E6E7EABF6FE8C2E73424D59097AB  
  
# install dependencies  
RUN apt-get update && apt-get --assume-yes install autoconf \  
automake \  
bc \  
build-essential \  
ccache \  
doxygen \  
git \  
git-lfs \  
help2man \  
libcfitsio-dev \  
libchealpix-dev \  
libfftw3-dev \  
libglib2.0-dev \  
libgsl0-dev \  
libhdf5-dev \  
liboctave-dev \  
libopenmpi-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
pkg-config \  
python-dev \  
python-h5py \  
python-healpy \  
python-numpy \  
python-openssl \  
python-pytest \  
python-pytest-mpl \  
python-reproject \  
python-scipy \  
python-setuptools \  
python-shapely \  
python-six \  
swig3.0 \  
texlive \  
wget  
  
# git-lfs post-install  
RUN git lfs install  
  
# clear package cache  
RUN rm -rf /var/lib/apt/lists/*  
  
# get source of unpackaged libraries  
RUN mkdir -p ~/src && \  
cd ~/src && \  
wget http://software.ligo.org/lscsoft/source/lscsoft-glue-1.58.2.tar.gz && \  
wget http://software.ligo.org/lscsoft/source/ligo-segments-1.0.0.tar.gz && \  
wget http://software.ligo.org/lscsoft/source/ldas-tools-al-2.5.7.tar.gz && \  
wget http://software.ligo.org/lscsoft/source/ldas-tools-framecpp-2.5.8.tar.gz
&& \  
wget http://software.ligo.org/lscsoft/source/libframe-8.30.tar.gz && \  
wget http://software.ligo.org/lscsoft/source/metaio-8.4.0.tar.gz || exit  
  
# glue  
RUN cd ~/src && \  
tar xf lscsoft-glue-1.58.2.tar.gz && \  
cd lscsoft-glue-1.58.2 && \  
python ./setup.py install --prefix=/usr/local && \  
cd ~/src && \  
rm -rf lscsoft-glue-1.58.2 || exit  
  
# ligo-segments  
RUN cd ~/src && \  
tar xf ligo-segments-1.0.0.tar.gz && \  
cd ligo-segments-1.0.0 && \  
python ./setup.py install --prefix=/usr/local && \  
cd ~/src && \  
rm -rf ligo-segments-1.0.0 || exit  
  
# ldas-tools-al  
RUN cd ~/src && \  
tar xf ldas-tools-al-2.5.7.tar.gz && \  
cd ldas-tools-al-2.5.7 && \  
./configure --prefix=/usr/local \  
\--disable-warnings-as-errors \  
\--disable-tcl \  
\--without-doxygen \  
\--enable-python \  
\--without-dot \  
\--disable-latex && \  
make && \  
make install && \  
cd ~/src && \  
rm -rf ldas-tools-al-2.5.7 && \  
ldconfig || exit  
  
# ldas-tools-frame-cpp  
RUN cd ~/src && \  
tar xf ldas-tools-framecpp-2.5.8.tar.gz && \  
cd ldas-tools-framecpp-2.5.8 && \  
./configure --prefix=/usr/local \  
\--disable-warnings-as-errors \  
\--disable-tcl \  
\--without-doxygen \  
\--enable-python \  
\--without-dot \  
\--disable-latex && \  
make && \  
make install && \  
cd ~/src && \  
rm -rf ldas-tools-framecpp-2.5.8 && \  
ldconfig || exit  
  
# libframe  
RUN cd ~/src && \  
tar xf libframe-8.30.tar.gz && \  
cd libframe-8.30 && \  
./configure --prefix=/usr/local && \  
make && \  
make install && \  
cd ~/src && \  
rm -rf libframe-8.30 && \  
ldconfig || exit  
  
# metaio  
RUN cd ~/src && \  
tar xf metaio-8.4.0.tar.gz && \  
cd metaio-8.4.0 && \  
./configure --prefix=/usr/local && \  
make && \  
make install && \  
cd ~/src && \  
rm -rf metaio-8.4.0 && \  
ldconfig || exit  

