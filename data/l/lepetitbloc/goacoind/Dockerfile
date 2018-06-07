ARG BDB_VERSION="4.8.30.NC"  
FROM lepetitbloc/bdb:$BDB_VERSION  
  
ARG USE_UPNP=1  
ENV USE_UPNP=$USE_UPNP  
  
EXPOSE 9999 1948  
RUN apt-get update -y && apt-get install -y \  
libssl-dev \  
libboost-system-dev \  
libboost-filesystem-dev \  
libboost-chrono-dev \  
libboost-program-options-dev \  
libboost-test-dev \  
libboost-thread-dev \  
libminiupnpc-dev \  
libqrencode-dev \  
libgmp-dev \  
libevent-dev \  
libzmq3-dev \  
automake \  
pkg-config \  
git \  
bsdmainutils \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -lrUm goacoin \  
&& git clone \--depth 1 https://github.com/goacoincore/goacoin.git
/tmp/goacoin  
  
WORKDIR /tmp/goacoin  
  
# build  
RUN chmod +x autogen.sh share/genbuild.sh src/leveldb/build_detect_platform \  
&& ./autogen.sh \  
&& ./configure CPPFLAGS="-I/usr/local/db4/include -O2"
LDFLAGS="-L/usr/local/db4/lib" \  
&& make \  
&& strip src/goacoind src/goacoin-cli src/goacoin-tx \  
&& mv src/goacoind /usr/local/bin/ \  
&& mv src/goacoin-cli /usr/local/bin/ \  
&& mv src/goacoin-tx /usr/local/bin/ \  
# clean  
&& rm -rf /tmp/goacoin  
  
USER goacoin  
  
WORKDIR /home/goacoin  
  
RUN mkdir -p .goacoincore data conf \  
&& touch conf/wallet.conf \  
&& ln -s conf/wallet.conf .goacoincore/goacoin.conf  
  
ENTRYPOINT ["/usr/local/bin/goacoind", "-reindex", "-printtoconsole",
"-logtimestamps=1", "-datadir=data", "-conf=../conf/wallet.conf",
"-mnconf=../conf/masternode.conf", "-port=9999", "-rpcport=1948"]  
CMD ["-rpcuser=goacoinrpc",
"-rpcpassword=4VvDhcoqFUcZbmkWUMJz8P443WLfoaMmiREKSByJaT4j",
"-rpcallowip=127.0.0.1", "-server=1", "-listen=0", "-masternode=0"]  

