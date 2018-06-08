FROM ubuntu:xenial  
MAINTAINER Bity DevOps <devops@bity.com>  
  
ARG USER_ID  
ARG GROUP_ID  
  
ENV HOME /litecoin  
  
# add user with specified (or default) user/group ids  
ENV USER_ID ${USER_ID:-1000}  
ENV GROUP_ID ${GROUP_ID:-1000}  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -g ${GROUP_ID} litecoin \  
&& useradd -u ${USER_ID} -g litecoin -s /bin/bash -m -d /litecoin litecoin  
  
# download litecoin  
ENV LITECOIN_VERSION=0.13.2  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-key FE3348877809386C \  
&& wget
https://download.litecoin.org/litecoin-${LITECOIN_VERSION}/linux/litecoin-${LITECOIN_VERSION}-x86_64-linux-
gnu.tar.gz \  
&& tar --strip=2 -xzf litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz -C
/usr/local/bin \  
&& rm litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz \  
&& apt-get purge -y \  
ca-certificates \  
wget \  
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
  
# bity additions for cryptogateway interactions  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-pip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& pip install pika unipath  
  
COPY ./bin /usr/local/bin  
COPY docker-entrypoint.sh /usr/local/bin/  
  
VOLUME ["/litecoin"]  
EXPOSE 9332 9333 19332 19333 19444  
WORKDIR /litecoin  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["ltc_oneshot"]  

