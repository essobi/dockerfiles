FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
build-essential \  
cmake \  
curl \  
g++ \  
git \  
libtool \  
libjson0 \  
libjson0-dev \  
pkg-config \  
python \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN sh -c 'echo "deb http://emdebian.org/tools/debian/ jessie main" >>
/etc/apt/sources.list.d/crosstools.list'  
RUN curl http://emdebian.org/tools/debian/emdebian-toolchain-archive.key |
apt-key add -  
RUN dpkg --add-architecture armhf  
RUN apt-get update && apt-get install -y \  
crossbuild-essential-armhf \  
pkg-config:armhf \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /xandev  
RUN mkdir /shared  
VOLUME ["/shared"]  
  
RUN cd /xandev && \  
wget http://download.libsodium.org/libsodium/releases/libsodium-1.0.8.tar.gz
&& \  
tar -zxvf libsodium-1.0.8.tar.gz && \  
cd libsodium-1.0.8 && \  
./configure --host=arm-linux-gnueabihf --prefix=/usr/arm-linux-gnueabihf && \  
make install && \  
ldconfig  
  
RUN cd /xandev && \  
wget http://download.zeromq.org/zeromq-4.1.4.tar.gz && \  
tar -zxvf zeromq-4.1.4.tar.gz && \  
cd zeromq-4.1.4 && \  
./configure --host=arm-linux-gnueabihf --prefix=/usr/arm-linux-gnueabihf && \  
make install && \  
ldconfig  
  
RUN cd /xandev && \  
wget http://download.zeromq.org/czmq-3.0.2.tar.gz && \  
tar -zxvf czmq-3.0.2.tar.gz && \  
cd czmq-3.0.2 && \  
./configure --host=arm-linux-gnueabihf --prefix=/usr/arm-linux-gnueabihf && \  
make install && \  
ldconfig  
  
RUN rm -rf /xandev

