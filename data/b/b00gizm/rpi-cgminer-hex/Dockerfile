# Custom cgminer build for HEX miners for running on your Raspberry Pi  
#  
# VERSION 0.0.1  
FROM resin/rpi-raspbian  
MAINTAINER Pascal Cremer <b00gizm@gmail.com>  
  
# Update packages  
RUN apt-get update  
  
# Basics  
RUN apt-get install -y git make curl  
  
# cgminer dependencies  
RUN apt-get install -y autoconf  
RUN apt-get install -y libtool  
RUN apt-get install -y libncurses-dev  
RUN apt-get install -y libudev-dev  
RUN apt-get install -y libcurl4-openssl-dev  
RUN apt-get install -y yasm  
RUN apt-get install -y pkg-config  
RUN apt-get install -y usbutils  
  
# Clone Github repo  
RUN git clone https://github.com/ckolivas/cgminer.git  
  
WORKDIR cgminer  
RUN git checkout 87f0213112a3c69e2c55160b9c674b9de2cde996  
RUN curl -L https://i.cloudup.com/GAkF6JdHG6.patch > cgminer.patch  
RUN patch -p1 < cgminer.patch  
  
# Compile & install  
RUN ./autogen.sh --disable-opencl --disable-adl --enable-hexminera --enable-
hexminerb --enable-hexminerc --enable-avalon  
RUN CFLAGS="-O2 -Wall -march=native" ./configure --disable-opencl --disable-
adl --enable-hexminera --enable-hexminerb --enable-hexminerc --enable-avalon  
RUN make  
RUN make install

