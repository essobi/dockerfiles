FROM ubuntu:17.10  
MAINTAINER BitbuyIO  
LABEL description="dockerized diamondd for running DMD Node"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
git software-properties-common build-essential libtool autotools-dev autoconf
\  
pkg-config libssl-dev libboost-all-dev libminiupnpc-dev bsdmainutils && \  
add-apt-repository ppa:bitcoin/bitcoin && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libdb4.8-dev libdb4.8++-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone https://github.com/dmdcoin/diamond.git /usr/src/diamond  
  
WORKDIR /usr/src/diamond  
  
RUN cd /usr/src/diamond && \  
./autogen.sh && \  
./configure && \  
make install && \  
rm -rf /usr/src/diamond  
  
ENV HOME /diamond  
  
VOLUME ["/diamond"]  
EXPOSE 17771 17772  
WORKDIR /diamond  
  
CMD ["dmd_oneshot"]  

