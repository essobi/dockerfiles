FROM ubuntu:12.04  
MAINTAINER saygox<ito.saygo@gmail.com>  
  
ENV LC_ALL C  
WORKDIR /tmp  
  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu precise main universe" >>
/etc/apt/sources.list  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y wget unzip lbzip2 make ia32-libs --no-install-recommends &&
\  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN \  
wget --no-check-certificate -O /tmp/legacy.zip
https://github.com/adamgreen/gcc4mbed/zipball/master && \  
mkdir -p /opt && \  
unzip -d /opt legacy.zip && \  
mv /opt/adamgreen-gcc4mbed-73e1ae9 /opt/gcc4mbed && \  
rm /tmp/legacy.zip && \  
cd /opt/gcc4mbed && \  
./linux_install  
  
ENV PATH /opt/gcc4mbed/gcc-arm-none-eabi/bin:$PATH  
ENV LPC_DEPLOY 'cp PROJECT.bin /media/MBED/ ; sync'  
ENV GCC4MBED_DIR /opt/gcc4mbed  
  
  
ENTRYPOINT []  
CMD ["make"]  

