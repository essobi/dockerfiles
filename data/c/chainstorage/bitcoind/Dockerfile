FROM ubuntu:16.04  
RUN groupadd --system --gid 19000 bitcoin \  
&& useradd --system --uid 19000 --create-home --gid bitcoin bitcoin  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -qq --no-install-recommends ca-certificates dirmngr
supervisor python-requests gpgv git wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV BITCOIN_VERSION 0.15.1  
ENV BITCOIN_URL https://bitcoin.org/bin/bitcoin-
core-0.15.1/bitcoin-0.15.1-x86_64-linux-gnu.tar.gz  
ENV BITCOIN_SHA256
387c2e12c67250892b0814f26a5a38f837ca8ab68c86af517f975a2a2710225b  
ENV BITCOIN_ASC_URL https://bitcoin.org/bin/bitcoin-core-0.15.1/SHA256SUMS.asc  
ENV BITCOIN_PGP_KEY 01EA5486DE18A882D4C2684590C8019E36C2E964  
  
# install bitcoin binaries  
RUN set -ex \  
&& BITCOIN_DIST=$(basename $BITCOIN_URL) \  
&& wget -qO $BITCOIN_DIST $BITCOIN_URL \  
&& echo "$BITCOIN_SHA256 $BITCOIN_DIST" | sha256sum -c - \  
&& gpg --keyserver keyserver.ubuntu.com --recv-keys $BITCOIN_PGP_KEY \  
&& wget -qO bitcoin.asc $BITCOIN_ASC_URL \  
&& gpg --verify bitcoin.asc \  
&& tar -xzvf $BITCOIN_DIST -C /usr/local \--strip-components=1 --exclude=*-qt
\  
&& rm bitcoin*  
  
RUN { set -ex; \  
mkdir /default; \  
mkdir /data; chown -R bitcoin:bitcoin /data; \  
mkdir /secrets; chown -R bitcoin:bitcoin /secrets;\  
mkdir /config; \  
mkdir /logs; \  
}  
VOLUME ["/data", "/secrets", "/config", "/logs"]  
  
COPY conf/* /default/  
  
# supervisor  
RUN { set -ex; \  
git clone https://github.com/chainstorage/CCUnRPC.git /usr/lib/python2.7/dist-
packages/ccunrpc/; \  
mkdir -p /var/run; \  
}  
  
COPY ep_lib.sh /ep_lib.sh  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8332 9001  

