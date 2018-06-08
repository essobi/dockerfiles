FROM phusion/baseimage:0.9.19  
  
ENV BITCOIND_REV master  
  
ARG UBUNTU_MIRROR=mirror://mirrors.ubuntu.com/mirrors.txt  
ARG BITCOIN_REPO=https://github.com/bitcoin/bitcoin.git  
  
RUN sed -i \  
-e s#http://archive.ubuntu.com/ubuntu/#${UBUNTU_MIRROR}#g \  
-e s#http://security.ubuntu.com/ubuntu/#${UBUNTU_MIRROR}#g \  
/etc/apt/sources.list ; \  
cat /etc/apt/sources.list  
  
RUN \  
apt-get update && \  
apt-get install -y \  
automake \  
autotools-dev \  
bsdmainutils \  
build-essential \  
git \  
libboost-chrono-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libboost-system-dev \  
libboost-test-dev \  
libboost-thread-dev \  
libevent-dev \  
libminiupnpc-dev \  
libssl-dev \  
libtool \  
libzmq3-dev \  
libzmq5 \  
pkg-config \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
git clone $BITCOIN_REPO /usr/local/src/bitcoin && \  
cd /usr/local/src/bitcoin && \  
git checkout $BITCOIND_REV && \  
./autogen.sh && \  
./configure --disable-wallet --enable-hardening && \  
make -j2 && \  
make install && \  
cd / && \  
rm -rf /usr/local/src/bitcoin  
  
RUN \  
apt-get remove -y \  
automake \  
autotools-dev \  
bsdmainutils \  
build-essential \  
git \  
libtool \  
pkg-config \  
&& \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HOME /var/lib/bitcoind  
RUN useradd -s /bin/bash -m -d /var/lib/bitcoind bitcoind  
RUN chown bitcoind:bitcoind -R /var/lib/bitcoind  
  
VOLUME ["/var/lib/bitcoind"]  
  
EXPOSE 8332  
  
EXPOSE 8333  
  
RUN mkdir -p /etc/service/bitcoind  
ADD bitcoind.run /etc/service/bitcoind/run  
  
RUN mkdir -p /etc/service/bitcoind/log  
ADD bitcoind.log.run /etc/service/bitcoind/log/run  
  
RUN chmod +x /etc/service/bitcoind/log/run \  
/etc/service/bitcoind/run  

