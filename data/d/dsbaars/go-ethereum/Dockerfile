FROM golang:1.6-wheezy  
MAINTAINER dsbaars  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get upgrade -q -y && \  
apt-get dist-upgrade -q -y  
  
RUN apt-get install -y build-essential libgmp3-dev git-core  
RUN git clone https://github.com/ethereum/go-ethereum /tmp/go-ethereum  
  
WORKDIR /tmp/go-ethereum  
RUN git checkout swarm  
RUN make geth  
  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
RUN apt-get remove --purge -y build-essential git-core  
RUN apt-get autoremove -y  
RUN apt-get autoclean -y  
  
EXPOSE 8545  
EXPOSE 30303  
RUN cp /tmp/go-ethereum/build/bin/geth /usr/local/bin/geth  
RUN rm -Rf /tmp/go-ethereum/  
  
RUN chmod +x /usr/local/bin/geth  
RUN adduser --disabled-password --gecos '' geth  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENV GETH_USER geth  
  
ENTRYPOINT ["/entrypoint.sh"]  

