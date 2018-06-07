FROM ubuntu:14.04  
MAINTAINER Milijan  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update  
RUN apt-get install -y csh  
RUN apt-get install -y gcc-4.8  
RUN apt-get install -y g++  
RUN apt-get install -y gfortran  
RUN apt-get install -y cmake  
RUN apt-get install -y libboost-all-dev  
RUN apt-get install -y git  
RUN apt-get install -y subversion  
RUN apt-get install -y wget  
RUN apt-get install -y unzip  
RUN apt-get install -y pkg-config  
RUN apt-get install -y autotools-dev  
RUN apt-get install -y automake  
RUN apt-get install -y autoconf  
RUN apt-get install -y build-essential libtool  
RUN apt-get install -y libgeotiff-dev  
RUN apt-get install -y xserver-xorg-dev  
RUN apt-get install -y xorg-dev  
RUN apt-get install -y libx11-dev  
RUN apt-get install -y libxext-dev  
RUN apt-get install -y libxmu6  
RUN apt-get install -y libxmu-dev  
RUN apt-get install -y libxi-dev  
RUN apt-get install -y libgl1-mesa-dev  
RUN apt-get install -y libglu1-mesa-dev  
RUN apt-get install -y freeglut3-dev  
  
# JPEG2000 support  
RUN cd /opt && git clone https://github.com/uclouvain/openjpeg.git && cd
openjpeg && git checkout tags/v2.1.1  
RUN mkdir /opt/openjpeg/build && cd /opt/openjpeg/build && cmake .. && make
-j$(nproc) && make install  
# satellite imaging metadata reader  
RUN cd /opt && wget http://download.osgeo.org/gdal/2.1.1/gdal211.zip && unzip
gdal211.zip  
RUN cd /opt/gdal-2.1.1 && ./configure && make -j$(nproc) && make install  
RUN rm /opt/gdal211.zip  
# LAS compression  
RUN cd /opt && git clone https://github.com/LASzip/LASzip.git && cd LASzip &&
git checkout tags/v2.2.0  
RUN cd /opt/LASzip && ./autogen.sh && ./configure
--includedir=/usr/local/include/laszip && make -j$(nproc) && make install  
# libLAS  
RUN cd /opt && git clone git://github.com/libLAS/libLAS.git && cd libLAS &&
git checkout tags/1.8.0  
RUN mkdir /opt/libLAS/makefiles && cd /opt/libLAS/makefiles && cmake -G "Unix
Makefiles" ../ && make -j$(nproc) && make install  
RUN ln -s /usr/lib/libproj.so.0 /usr/lib/libproj.so  
  

