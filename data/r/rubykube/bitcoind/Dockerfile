FROM debian:8 as builder  
  
ENV BITCOIN_VERSION 0.15.1  
RUN apt-get update  
RUN apt-get install -y wget curl build-essential libtool \  
autotools-dev automake pkg-config \  
libssl-dev libevent-dev bsdmainutils python3 \  
libboost-system-dev libboost-filesystem-dev libboost-chrono-dev \  
libboost-program-options-dev libboost-test-dev libboost-thread-dev  
  
RUN wget https://github.com/bitcoin/bitcoin/archive/v${BITCOIN_VERSION}.tar.gz  
RUN tar vzxf v${BITCOIN_VERSION}.tar.gz  
RUN cd bitcoin-${BITCOIN_VERSION} && ./autogen.sh && \  
./configure --disable-wallet --without-gui --without-miniupnpc && \  
make -j && \  
make install  
  
FROM debian:stable-slim as runtime  
  
COPY \--from=builder /usr/local/bin/bitcoin* /usr/local/bin/  
  
# Create bitcoin user  
ENV BITCOIN_HOME /bitcoin  
  
RUN groupadd -g 1000 bitcoin \  
&& useradd -u 1000 -g bitcoin -s /bin/bash -m -d ${BITCOIN_HOME} bitcoin  
  
# Prepare bitcoin config  
RUN mkdir ${HOME}/.bitcoin  
ADD config/bitcoin.conf ${HOME}/.bitcoin  
RUN chown bitcoin:bitcoin -R $BITCOIN_HOME  
  
USER bitcoin  
  
EXPOSE 19000 19001  
CMD ["bitcoind"]  

