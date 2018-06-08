FROM ubuntu:xenial  
EXPOSE 8333  
VOLUME /var/bitcoin  
RUN apt update -y \  
&& apt install -y software-properties-common \  
&& add-apt-repository ppa:bitcoin/bitcoin -yu \  
&& apt install -y build-essential libtool autotools-dev automake pkg-config
libssl-dev \  
libevent-dev bsdmainutils libdb4.8-dev libdb4.8++-dev libboost-system-dev \  
libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev \  
libboost-test-dev libboost-thread-dev git libminiupnpc-dev \  
&& git clone https://github.com/Bitcoin-ABC/bitcoin-abc \  
&& cd bitcoin-abc \  
&& ./autogen.sh \  
&& ./configure --without-gui --with-miniupnpc \  
&& make \  
&& make install \  
&& mkdir -p /var/bitcoin  
CMD ["bitcoind", "-printtoconsole", "-datadir=/var/bitcoin", "-upnp"]  

