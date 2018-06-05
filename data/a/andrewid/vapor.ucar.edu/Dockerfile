FROM debian:buster-slim  
MAINTAINER András Kiss  
ENV VAPOR_VERSION 2.6.0  
WORKDIR /usr/src  
COPY options.mk /usr/src/  
RUN apt-get update && \  
apt-get install -y wget \  
libassimp-dev \  
libfreetype6-dev \  
libftgl-dev \  
libglew-dev \  
libgrib-api-dev \  
libhdf5-dev \  
libjpeg-dev \  
libgeotiff-dev \  
libnetcdf-dev \  
libtiff-dev \  
libproj-dev \  
python \  
libqt4-dev \  
make \  
g++ \  
python-dev \  
libudunits2-dev \  
python-numpy \  
tightvncserver && \  
apt-get clean && \  
wget
https://www.vapor.ucar.edu/sites/default/files/attachments/vapor-$VAPOR_VERSION-
src.tar.gz && \  
tar xf vapor-$VAPOR_VERSION-src.tar.gz && \  
mv options.mk vapor-$VAPOR_VERSION/ && \  
rm vapor-$VAPOR_VERSION-src.tar.gz && \  
ln -s /usr/include/qt4/* /usr/include/ && \  
cd vapor-$VAPOR_VERSION && \  
make && \  
make install && \  
cd .. && \  
rm -rf vapor-$VAPOR_VERSION  
  
  

