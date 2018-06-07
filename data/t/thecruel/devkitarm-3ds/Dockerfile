FROM ubuntu:zesty  
MAINTAINER Thomas Edvalson "machin3@gmail.com"  
ENV DEVKITPRO /opt/devkitPro  
ENV DEVKITARM $DEVKITPRO/devkitARM  
ENV CTRULIB $DEVKITPRO/libctru  
ENV PORTLIBS $DEVKITPRO/portlibs/armv6k  
  
RUN apt-get update && apt-get -y install \  
automake \  
autogen \  
build-essential \  
bzip2 \  
ca-certificates \  
cmake \  
curl \  
file \  
git \  
gzip \  
libssl-dev \  
make \  
ncurses-dev \  
pkg-config \  
python \  
rsync \  
sed \  
tar \  
wget \  
xz-utils  
  
RUN apt-get -y clean  
  
RUN wget
https://sourceforge.net/projects/devkitpro/files/devkitARM/devkitARM_r46/devkitARM_r46-x86_64-linux.tar.bz2
-O dka.tar.bz2 && \  
mkdir $DEVKITPRO && \  
tar -xaf dka.tar.bz2 -C $DEVKITPRO && \  
rm dka.tar.bz2  
  
RUN git clone https://github.com/smealum/ctrulib.git && \  
cd ctrulib/libctru && make -j4 install && cd \- && \  
rm -r ctrulib  
  
RUN git clone https://github.com/fincs/citro3d.git && \  
cd citro3d && make -j4 install && cd \- && \  
rm -r citro3d  

