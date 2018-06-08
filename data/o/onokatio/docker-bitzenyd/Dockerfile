FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential \  
libtool autotools-dev autoconf \  
libssl-dev \  
libboost-all-dev \  
pkg-config \  
software-properties-common \  
git && \  
add-apt-repository -y ppa:bitcoin/bitcoin && \  
apt-get update && \  
apt-get install -y libdb4.8-dev libdb4.8++-dev && \  
git clone https://github.com/bitzeny/bitzeny.git && \  
cd bitzeny && \  
./autogen.sh && \  
./configure --prefix=/usr --without-miniupnpc --without-gui --disable-tests &&
\  
make && make install && \  
cd .. && \  
rm -fr bitzeny && \  
apt-get autoremove -y build-essential \  
autoconf \  
pkg-config \  
software-properties-common \  
git && \  
apt-get clean -y  
  
VOLUME /root/.bitzeny  
EXPOSE 9252 9253  
  
ENTRYPOINT [ "/usr/bin/bitzenyd" ]  

