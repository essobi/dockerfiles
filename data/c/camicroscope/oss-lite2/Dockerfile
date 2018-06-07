############################################################  
# Dockerfile to build Oss-lite container images  
# Based on Ubuntu  
############################################################  
FROM ubuntu:14.04  
  
MAINTAINER Sapoonjyoti DuttaDuwarah  
### update  
RUN apt-get -q -y update  
RUN apt-get -q -y upgrade  
RUN apt-get -q -y dist-upgrade  
RUN apt-get -q -y install openssh-server  
RUN apt-get -q -y install curl  
  
RUN apt-get -q -y install build-essential \  
python \  
python-dev \  
python-distribute \  
python-pip \  
git \  
openslide-tools \  
python-openslide  
  
RUN pip install flask \  
gunicorn  
  
### prereqs for openslide  
RUN apt-get -q -y install zlib1g-dev libpng12-dev libjpeg-dev libtiff5-dev
libgdk-pixbuf2.0-dev libxml2-dev libsqlite3-dev libcairo2-dev libglib2.0-dev  
  
### need build tools for building openslide and later iipsrv  
RUN apt-get -q -y install git autoconf automake make libtool pkg-config cmake  
  
RUN mkdir /root/src  
  
WORKDIR /root/src  
#Libraries that are needed for openslide  
RUN curl -O -J -L http://downloads.sourceforge.net/lcms/lcms2-2.7.tar.gz && \  
tar -xzvf lcms2-2.7.tar.gz && \  
cd lcms2-2.7 && ./configure && \  
make -j4 && make install && \  
cd .. && rm -rf lcms2-2.7*  
  
RUN curl -O -J -L http://downloads.sourceforge.net/libpng/libpng-1.6.22.tar.xz
&& \  
tar -xvf libpng-1.6.22.tar.xz && \  
cd libpng-1.6.22 && ./configure && \  
make -j4 && make install && \  
cd .. && rm -rf libpng-1.6.22*  
  
RUN curl -O -J -L http://download.osgeo.org/libtiff/tiff-4.0.6.tar.gz && \  
tar -xzvf tiff-4.0.6.tar.gz && \  
cd tiff-4.0.6 && ./configure && \  
make -j4 && make install && \  
cd .. && rm -rf tiff-4.0.6*  
  
#RUN apt-get install cmake3  
RUN curl -O -J -L
http://downloads.sourceforge.net/openjpeg.mirror/openjpeg-2.1.0.tar.gz && \  
tar -xzvf openjpeg-2.1.0.tar.gz && \  
cd openjpeg-2.1.0 && mkdir build && \  
cd build && cmake ../ && \  
make -j4 && make install && \  
cd ../.. && rm -rf openjpeg-2.1.0*  
  
### Openslide  
WORKDIR /root/src  
RUN git clone https://github.com/openslide/openslide.git  
  
## build openslide  
WORKDIR /root/src/openslide  
RUN git checkout tags/v3.4.1  
RUN autoreconf -i  
#RUN ./configure --enable-static --enable-shared=no  
# may need to set OPENJPEG_CFLAGS='-I/usr/local/include' and
OPENJPEG_LIBS='-L/usr/local/lib -lopenjp2'  
# and the corresponding TIFF flags and libs to where bigtiff lib is installed.  
RUN ./configure  
RUN make  
RUN make install  
  
WORKDIR /root/src  
  
RUN git clone --recursive https://github.com/camicroscope/oss-lite.git  
  
  
WORKDIR /root/src/oss-lite  
  
CMD ["sh", "run.sh"]  

