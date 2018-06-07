# Based on ideas from amacneil/bitcoin and kylemanna/docker-bitcoind.  
# To build:  
# docker build -t futurelabs/litecoin-core .  
FROM buildpack-deps:jessie-curl  
  
MAINTAINER FutureLabs  
LABEL vendor=ru.ruturelabs  
LABEL service=litecoin-core  
LABEL service-version=0.10.4.0  
  
ENV LITECOIN_VERSION 0.10.4.0  
ENV LITECOIN_URL
https://download.litecoin.org/litecoin-$LITECOIN_VERSION/linux/litecoin-$LITECOIN_VERSION-
linux64.tar.gz  
ENV LITECOIN_ASC_URL
https://download.litecoin.org/litecoin-$LITECOIN_VERSION/linux/litecoin-$LITECOIN_VERSION-
linux64.tar.gz.asc  
  
ENV USERNAME litecoin  
ENV LITECOIN_DATA /litecoin  
ENV HOME $LITECOIN_DATA  
  
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
&& LITECOIN_DIST=$(basename $LITECOIN_URL) \  
&& wget -O $LITECOIN_DIST $LITECOIN_URL \  
# Validate the binaries \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
59CAF0E96F23F53747945FD4FE3348877809386C \  
&& wget -qO litecoin.asc $LITECOIN_ASC_URL \  
&& gpg --verify litecoin.asc $LITECOIN_DIST \  
&& tar -xzvf $LITECOIN_DIST -C /usr/local \--strip-components=1 --exclude=*-qt
\  
&& rm litecoin.asc $LITECOIN_DIST \  
&& chown -R $USERNAME:$USERNAME $HOME \  
&& ln -s $LITECOIN_DATA $HOME/.litecoin  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
USER $USERNAME  
VOLUME $HOME  
WORKDIR /litecoin  
  
EXPOSE 9332 9333 19332 19333  
CMD ["litecoind"]  

