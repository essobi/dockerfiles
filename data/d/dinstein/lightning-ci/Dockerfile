FROM ubuntu:xenial  
MAINTAINER Linfeng Liang <lianglinfeng@gmail.com>  
  
ENV HOME /build  
  
RUN useradd -ms /bin/bash builder \  
&& mkdir /build && chown builder /build  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8842ce5e && \  
echo "deb http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu xenial main" >
/etc/apt/sources.list.d/bitcoin.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl git make automake autoconf libtool bitcoind build-essential libprotobuf-
c-dev libsodium-dev libbase58-dev libsqlite3-dev libgmp-dev libsqlite3-dev git
net-tools \  
valgrind \  
ca-certificates python3 python\  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# grab gosu for easy step-down from root  
# ENV GOSU_VERSION 1.7  
# RUN set -x \  
# && apt-get update && apt-get install -y --no-install-recommends \  
# ca-certificates \  
# wget \  
# && wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
# && wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
# && export GNUPGHOME="$(mktemp -d)" \  
# && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
# && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
# && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
# && chmod +x /usr/local/bin/gosu \  
# && gosu nobody true \  
# && apt-get purge -y \  
# ca-certificates \  
# wget \  
# && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /build  
  
#USER builder  

