FROM debian:stretch-slim as builder  
ENV LIGHTNINGD_VERSION=master  
  
RUN set -x && \  
apt-get update -qq && \  
apt-get install -qq -y --no-install-recommends --allow-unauthenticated \  
python \  
python3 \  
git \  
make \  
automake \  
autoconf \  
libtool \  
build-essential \  
libprotobuf-c-dev \  
libsodium-dev \  
libbase58-dev \  
libsqlite3-dev \  
libgmp-dev \  
ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
RUN set -x && \  
git clone https://github.com/ElementsProject/lightning.git /opt/lightningd &&
\  
cd /opt/lightningd && \  
git checkout $LIGHTNINGD_VERSION && \  
make && \  
cp \  
lightningd/lightningd \  
lightningd/lightning_channeld \  
lightningd/lightning_closingd \  
lightningd/lightning_gossipd \  
lightningd/lightning_hsmd \  
lightningd/lightning_onchaind \  
lightningd/lightning_openingd \  
cli/lightning-cli \  
/usr/local/bin/ && \  
rm -rf /opt/lightningd  
  
FROM vtorhonen/bitcoind:0.15.1-1  
  
COPY \--from=builder /usr/local/bin /usr/local/bin  
  
RUN set -x && \  
apt-get update -qq && \  
apt-get install -qq -y --no-install-recommends \  
libgcc1 \  
libgmp10 \  
libsodium-dev \  
libsqlite3-dev && \  
rm -rf /var/lib/apt/lists/*  
  
CMD []  
ENTRYPOINT []

