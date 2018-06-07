FROM debian:stretch-slim  
  
RUN groupadd -r bitcoin && useradd -r -m -g bitcoin bitcoin  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -qq --no-install-recommends ca-certificates dirmngr gosu
gpg wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV BITCOIN_VERSION=0.15.1 \  
BITCOIN_URL=https://bitcoincore.org/bin/bitcoin-
core-0.15.1/bitcoin-0.15.1-aarch64-linux-gnu.tar.gz \  
BITCOIN_SHA256=d64d2e27cad78bbd2a0268bdaa9efa3f1eca670a4fab462b5e851699c780e3a0
\  
BITCOIN_ASC_URL=https://bitcoincore.org/bin/bitcoin-core-0.15.1/SHA256SUMS.asc
\  
BITCOIN_PGP_KEY=01EA5486DE18A882D4C2684590C8019E36C2E964 \  
BITCOIN_DATA=/data  
  
# install bitcoin binaries  
RUN set -ex \  
&& cd /tmp \  
&& wget -qO bitcoin.tar.gz "$BITCOIN_URL" \  
&& echo "$BITCOIN_SHA256 bitcoin.tar.gz" | sha256sum -c - \  
&& gpg --keyserver keyserver.ubuntu.com --recv-keys "$BITCOIN_PGP_KEY" \  
&& wget -qO bitcoin.asc "$BITCOIN_ASC_URL" \  
&& gpg --verify bitcoin.asc \  
&& tar -xzvf bitcoin.tar.gz -C /usr/local \--strip-components=1 --exclude=*-qt
\  
&& rm -rf /tmp/*  
  
# create data directory  
RUN mkdir "$BITCOIN_DATA" \  
&& chown -R bitcoin:bitcoin "$BITCOIN_DATA" \  
&& ln -sfn "$BITCOIN_DATA" /home/bitcoin/.bitcoin \  
&& chown -h bitcoin:bitcoin /home/bitcoin/.bitcoin  
  
VOLUME /data  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bitcoind"]  

