FROM debian:stable  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386  
RUN apt-get update  
  
# toolchain  
RUN apt-get install -y \  
libstdc++6:i386 \  
libgcc1:i386 \  
zlib1g:i386  
  
# compilers  
RUN apt-get install -y g++  
  
# tools  
RUN apt-get install -y \  
scons \  
gengetopt \  
wget \  
unzip \  
qemu  
  
# dependencies  
RUN apt-get install -y \  
libtool \  
intltool \  
autoconf \  
automake \  
make \  
cmake  
  
RUN wget -O /tmp/tools-master.zip \  
https://codeload.github.com/raspberrypi/tools/zip/master && \  
unzip /tmp/tools-master.zip -d /tmp && \  
mv /tmp/tools-master/arm-bcm2708 /opt/toolchains && \  
rm -rf /tmp/tools-master && \  
rm /tmp/tools-master.zip  

