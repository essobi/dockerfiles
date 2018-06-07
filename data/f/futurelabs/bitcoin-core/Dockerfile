# Based on ideas from amacneil/bitcoin and kylemanna/docker-bitcoind.  
# To build:  
# docker build -t futurelabs/bitcoin-core .  
FROM buildpack-deps:jessie-curl  
  
MAINTAINER FutureLabs  
LABEL vendor=ru.ruturelabs  
LABEL service=bitcoin-core  
LABEL service-version=0.12.0  
  
ENV BITCOIN_VERSION 0.12.0  
ENV BITCOIN_URL https://bitcoin.org/bin/bitcoin-
core-$BITCOIN_VERSION/bitcoin-$BITCOIN_VERSION-linux64.tar.gz  
ENV BITCOIN_ASC_URL https://bitcoin.org/bin/bitcoin-
core-$BITCOIN_VERSION/SHA256SUMS.asc  
  
ENV USERNAME bitcoin  
ENV BITCOIN_DATA /bitcoin  
ENV HOME $BITCOIN_DATA  
  
RUN \  
# Create user, and its directory \  
groupadd --system $USERNAME && useradd --system --gid $USERNAME \--create-home
--home-dir $HOME $USERNAME \  
&& set -ex \  
# Grab gosu for easy step-down from root. \  
# This image is shared with every other Dockerfile build in the same fashion.
\  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& wget -qO /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" \  
&& wget -qO /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
# Install the binaries \  
&& BITCOIN_DIST=$(basename $BITCOIN_URL) \  
&& wget -O $BITCOIN_DIST $BITCOIN_URL \  
# Validate the binaries \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
01EA5486DE18A882D4C2684590C8019E36C2E964 \  
&& wget -qO bitcoin.asc $BITCOIN_ASC_URL \  
&& gpg --verify bitcoin.asc \  
&& tar -xzvf $BITCOIN_DIST -C /usr/local \--strip-components=1 --exclude=*-qt
\  
&& rm bitcoin.asc $BITCOIN_DIST \  
&& chown -R $USERNAME:$USERNAME $HOME \  
&& ln -s $BITCOIN_DATA $HOME/.bitcoin  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
USER $USERNAME  
VOLUME $HOME  
WORKDIR /bitcoin  
  
EXPOSE 9332 9333 19332 19333  
CMD ["bitcoind"]  

