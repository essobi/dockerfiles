FROM debian:latest  
MAINTAINER peerchemist <peerchemist@protonmail.ch> (@peerboxPPC)  
  
ENV PPC_VERSION=0.5.4pars  
ENV PPC_SHA256
0eadf070acdc6d926bc45e98effe6fb2205ab811257eef105f2520eb08527d2b  
ENV GOSU_VERSION=1.9  
  
# build  
## dependencies  
RUN apt-get update -y \  
&& apt-get install \--no-install-recommends -y curl ca-certificates build-
essential libssl-dev libdb++-dev \  
libboost-program-options-dev libboost-filesystem-dev libboost-system-dev
libboost-thread-dev \  
libboost-program-options1.55.0 libboost-filesystem1.55.0 libboost-system1.55.0
libboost-thread1.55.0 \  
tor \  
## gosu  
&& gpg \--keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -fSL
https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture) \  
&& curl -o /usr/local/bin/gosu.asc -fSL
https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture).asc \  
&& gpg \--verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
## ppcoind  
&& curl -SLO4 https://github.com/hrobeers/peercoin-advanced-
relay/archive/v${PPC_VERSION}.tar.gz \  
&& tar xf v${PPC_VERSION}.tar.gz \  
&& echo "$PPC_SHA256 v${PPC_VERSION}.tar.gz" | sha256sum -c - \  
&& cd peercoin-advanced-relay-${PPC_VERSION} \  
## make ppcoind  
&& make -f makefile.unix USE_UPNP= -e PIE=1 -C src \  
&& install -Dm755 "src/ppcoind" "/usr/local/bin/" \  
## cleanup  
&& cd .. && rm v${PPC_VERSION}.tar.gz && rm -r peercoin-advanced-
relay-${PPC_VERSION} \  
&& apt-get remove -y \--purge curl ca-certificates build-essential libssl-dev
libdb++-dev \  
libboost-program-options-dev libboost-filesystem-dev libboost-system-dev
libboost-thread-dev \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& useradd -r sunny  
  
#tor stuff  
#https://github.com/peerchemist/Peerbox/blob/3c8e2e25cb0589624cfff15de6b78f6b507eb08d/pcf/set_tor  
RUN echo "HiddenServiceDir /var/lib/tor/ppcoin-service/" >> /etc/tor/torrc &&
echo "HiddenServicePort 9901 127.0.0.1:9901" >> /etc/tor/torrc  
## container stuff  
ENV PPC_DATA=/home/sunny/.ppcoin \  
PATH=/usr/local/bin/:$PATH  
VOLUME ["/home/sunny/.ppcoin"]  
  
COPY entrypoint-tor.sh /entrypoint-tor.sh  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 9901 9902 9903 9904  
CMD ["ppcoind"]  

