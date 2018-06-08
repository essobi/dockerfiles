FROM ubuntu:16.04  
  
RUN apt-get update -y && \  
apt-get dist-upgrade -y  
  
ENV REPO https://github.com/segsignal/bitcoin.git  
ENV BRANCH segsignal-v0.14.2  
  
RUN apt-get install --no-install-recommends --no-install-suggests ca-
certificates git make build-essential libtool autotools-dev \  
automake pkg-config libssl-dev libevent-dev bsdmainutils libboost-system-dev
libboost-filesystem-dev \  
libboost-chrono-dev libboost-program-options-dev libboost-test-dev libboost-
thread-dev -y && \  
mkdir -p /tmp/build /var/bitcoind && \  
cd /tmp/build && \  
git clone -b $BRANCH $REPO && \  
cd bitcoin && \  
./autogen.sh && \  
./configure --disable-wallet --without-gui && \  
make && \  
make install && \  
useradd bitcoind -d /var/bitcoind && \  
chown bitcoind:bitcoind /var/bitcoind && \  
rm -R /tmp/build && \  
apt-get remove --purge ca-certificates git make build-essential libtool
autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils \  
libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-
program-options-dev libboost-test-dev libboost-thread-dev -y && \  
rm -rf /var/lib/apt/lists/*  
  
USER bitcoind  
VOLUME ["/var/bitcoind"]  
EXPOSE 8333  
CMD ["bitcoind"]  

