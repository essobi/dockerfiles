FROM ubuntu:16.04  
ENV HOME /wey  
  
# Install dependecies  
RUN apt-get update -q  
RUN apt-get -qq -y install \  
wget \  
git \  
gcc \  
software-properties-common \  
build-essential \  
libtool \  
autotools-dev \  
autoconf \  
automake \  
libssl-dev \  
libevent-dev \  
libboost-all-dev \  
pkg-config  
  
RUN add-apt-repository -y ppa:bitcoin/bitcoin  
RUN apt-get update -q && apt-get -qq -y install \  
libdb4.8-dev \  
libdb4.8++-dev \  
libminiupnpc-dev \  
libzmq3-dev \  
libevent-pthreads-2.0-5 \  
libqt5gui5 \  
libqt5core5a \  
libqt5dbus5 \  
qttools5-dev \  
qttools5-dev-tools \  
libprotobuf-dev \  
libqrencode-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone \--depth 1 -b 1.3.0.1 https://github.com/WeyCoin/WeyCoin.git  
WORKDIR /WeyCoin  
RUN ./autogen.sh  
RUN ./configure --disable-tests --disable-gui-tests --with-gui=no  
RUN make  
  
RUN strip ./src/weycoind  
RUN strip ./src/weycoin-cli  
  
FROM ubuntu:16.04  
RUN apt-get update -q  
RUN apt-get -qq -y install --no-install-recommends \  
software-properties-common  
RUN add-apt-repository -y ppa:bitcoin/bitcoin  
RUN apt-get update -q  
RUN apt-get -qq -y install --no-install-recommends \  
libminiupnpc-dev \  
libdb4.8-dev \  
libdb4.8++-dev \  
libevent-dev \  
libboost-all-dev \  
libzmq3-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /  
COPY \--from=0 /WeyCoin/src/weycoind /usr/local/bin/  
COPY \--from=0 /WeyCoin/src/weycoin-cli /usr/local/bin/  
COPY ./weycoin-masternode.sh ./  
COPY ./weycoin-default.conf ./  
  
RUN groupadd -r weycoin && useradd --no-log-init -m -d /wey -g weycoin weycoin  
RUN mkdir /wey/.weycoin/  
RUN chown weycoin:weycoin -R /wey  
  
RUN chmod a+x /usr/local/bin/*  
  
ENV MALLOC_ARENA_MAX=1  
VOLUME ["/wey/.weycoin/"]  
EXPOSE 11526  
WORKDIR /wey  
ENTRYPOINT [ "bash", "/weycoin-masternode.sh" ]  
USER weycoin  

