FROM ubuntu:xenial  
MAINTAINER Willy Ko <wko@blockchainfoundry.co>  
  
ARG USER_ID  
ARG GROUP_ID  
  
ENV HOME /syscoin  
  
# add user with specified (or default) user/group ids  
ENV USER_ID ${USER_ID:-1000}  
ENV GROUP_ID ${GROUP_ID:-1000}  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -g ${GROUP_ID} syscoin \  
&& useradd -u ${USER_ID} -g syscoin -s /bin/bash -m -d /syscoin syscoin  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
6C2343CF3DDDFC8DBAA94C02FCA4C13E83E54555 && \  
echo "deb http://ppa.launchpad.net/willyk/syscoin/ubuntu xenial main" >
/etc/apt/sources.list.d/syscoin.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
syscoind \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
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
&& apt-get purge -y \  
ca-certificates \  
wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ./bin /usr/local/bin  
  
VOLUME ["/syscoin"]  
  
EXPOSE 8332 8333 18332 18333  
WORKDIR /syscoin  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["sys_oneshot"]  

