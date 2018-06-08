FROM ubuntu:16.04  
ARG scorecoinVersion=2.0.0.1  
ARG _scorecoinBin=/opt/scorecoin/Scored  
ARG _entryPointBin=/opt/docker-entrypoint.sh  
  
ARG tarDirectory=Scorecoin-2.0  
ENV WALLET_CONF /etc/scorecoin/score.conf  
ENV WALLET_DATA /data/  
  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties
build-essential libssl-dev \  
libboost-all-dev libcrypto++-dev libqrencode-dev libminiupnpc-dev libgmp-dev \  
libgmp3-dev autoconf autogen automake libtool git \  
libevent-dev libminiupnpc-dev libssl-dev libboost-all-dev libcrypto++-dev
libqrencode-dev \  
libminiupnpc-dev libgmp-dev libgmp3-dev libtool \  
wget && \  
add-apt-repository ppa:bitcoin/bitcoin && \  
apt-get update && \  
apt-get install libdb4.8-dev libdb4.8++-dev -y && \  
apt-get purge -y python-software-properties  
  
COPY /docker-entrypoint.sh $_entryPointBin  
  
RUN mkdir -p `dirname $_scorecoinBin` && \  
cd `dirname $_scorecoinBin` && \  
wget
https://github.com/ddude1/Scorecoin/releases/download/$scorecoinVersion/Scored.gz
&& \  
gunzip Scored.gz && \  
chmod +x $_scorecoinBin && \  
ln -s $_scorecoinBin /usr/local/bin/scored && \  
chmod +x $_entryPointBin && \  
ln -s $_entryPointBin /usr/local/bin/docker-entry && \  
mkdir -p `dirname $WALLET_CONF`  
  
VOLUME /data  
  
EXPOSE 17075 22350  
ENTRYPOINT ["docker-entry"]  
  

