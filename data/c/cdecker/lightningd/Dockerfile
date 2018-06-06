FROM ubuntu:16.04  
ENV LIGHTNINGD_VERSION=master  
  
RUN echo deb http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu xenial main >
/etc/apt/sources.list.d/bitcoin-bitcoin-xenial.list && \  
apt-get update -qq && \  
apt-get install -qq -y \--no-install-recommends --allow-unauthenticated python
python3 git make automake autoconf libtool bitcoind build-essential
libprotobuf-c-dev libsodium-dev libbase58-dev libsqlite3-dev libgmp-dev
libsqlite3-dev git net-tools valgrind curl ca-certificates jq  
  
RUN git clone https://github.com/ElementsProject/lightning.git /opt/lightningd
&& \  
cd /opt/lightningd && \  
git checkout $LIGHTNINGD_VERSION && \  
make && cp lightningd/lightning* cli/lightning-cli /usr/bin/  

