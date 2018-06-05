ARG BDB_VERSION="4.8.30.NC"  
FROM lepetitbloc/bdb:$BDB_VERSION  
  
ARG USE_UPNP=1  
ENV USE_UPNP=$USE_UPNP  
  
EXPOSE 9918 9919  
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
&& useradd -lrUm desire \  
&& git clone \--depth 1 https://github.com/lazyboozer/Desire.git /tmp/desire  
WORKDIR /tmp/desire  
  
# build  
RUN chmod +x autogen.sh share/genbuild.sh src/leveldb/build_detect_platform \  
&& ./autogen.sh \  
&& ./configure CPPFLAGS="-I/usr/local/db4/include -O2"
LDFLAGS="-L/usr/local/db4/lib" \  
&& make \  
&& strip src/desired src/desire-cli src/desire-tx \  
&& mv src/desired /usr/local/bin/ \  
&& mv src/desire-cli /usr/local/bin/ \  
&& mv src/desire-tx /usr/local/bin/ \  
# clean  
&& rm -rf /tmp/desire  
  
USER desire  
  
WORKDIR /home/desire  
  
RUN mkdir -p .desire data  
  
COPY wallet/.desire/ .desire/  
  
ENTRYPOINT ["/usr/local/bin/desired", "-reindex", "-printtoconsole",
"-logtimestamps=1", "-datadir=data", "-conf=../.desire/desire.conf",
"-mnconf=../.desire/masternode.conf", "-port=9918", "-rpcport=9919"]  
CMD ["-rpcallowip=127.0.0.1", "-server=1", "-masternode=0"]  

