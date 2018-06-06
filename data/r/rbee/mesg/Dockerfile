FROM ubuntu:16.04  
  
ENV GOSU_VERSION=1.9 RABBITMQ_VERSION=3.6.5 RABBITMQ_DEBIAN_VERSION=3.6.5-1
HAPROXY_MAJOR=1.6 HAPROXY_VERSION=1.6.8
HAPROXY_MD5=8cb3719013e7f34c6d689dabf8a8cd6e  
ENV RBEE_AUTOKILL=true RABBITMQ_DEFAULT_USER=lupine
RABBITMQ_DEFAULT_PASS=bunny  
  
RUN set -x \  
# Add Users  
&& groupadd -r rabbitmq && useradd -r -d /var/lib/rabbitmq -m -g rabbitmq
rabbitmq \  
&& groupadd -r haproxy && useradd -r -m -g haproxy haproxy \  
  
# Update cache  
&& apt-get update \  
  
# Update base image (security updates)  
# && apt-get upgrade -y \  
# Install step #1. Some requirements for other installations  
&& apt-get install -y --no-install-recommends supervisor ca-certificates wget
libssl1.0.0 libpcre3 \  
  
  
  
# Download, verify and compile HAProxy  
&& buildDeps='curl gcc libc6-dev libpcre3-dev libssl-dev make' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& curl -SL
"http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz"
-o haproxy.tar.gz \  
&& echo "${HAPROXY_MD5} haproxy.tar.gz" | md5sum -c \  
&& mkdir -p /usr/src/haproxy \  
&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \  
&& rm haproxy.tar.gz \  
&& make -C /usr/src/haproxy \  
TARGET=linux2628 \  
USE_PCRE=1 PCREDIR= \  
USE_OPENSSL=1 \  
USE_ZLIB=1 \  
all \  
install-bin \  
&& mkdir -p /usr/local/etc/haproxy \  
&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \  
&& rm -rf /usr/src/haproxy  
  
# grab gosu for easy step-down from root  
RUN wget -O /usr/local/bin/gosu
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
  
  
# Add GPG keys, add repos, update and install Erlang and RabbitMQ  
&& apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
434975BD900CCBE4F7EE1B1ED208507CA14F4FCA \  
&& apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
0A9AF2115F4687BD29803A206B73A36E6026DFCA \  
&& echo 'deb http://packages.erlang-solutions.com/debian jessie contrib' >
/etc/apt/sources.list.d/erlang.list \  
&& echo 'deb http://www.rabbitmq.com/debian testing main' >
/etc/apt/sources.list.d/rabbitmq.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
erlang-asn1 \  
erlang-base-hipe \  
erlang-crypto \  
erlang-eldap \  
erlang-inets \  
erlang-mnesia \  
erlang-nox \  
erlang-os-mon \  
erlang-public-key \  
erlang-ssl \  
erlang-xmerl \  
rabbitmq-server=$RABBITMQ_DEBIAN_VERSION \  
  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
  
&& echo '[ { rabbit, [ { loopback_users, [ ] } ] } ].' >
/etc/rabbitmq/rabbitmq.config \  
&& mkdir -p /var/lib/rabbitmq /etc/rabbitmq \  
&& chown -R rabbitmq:rabbitmq /var/lib/rabbitmq /etc/rabbitmq \  
&& chmod 777 /var/lib/rabbitmq /etc/rabbitmq  
  
VOLUME /var/lib/rabbitmq  
  
RUN ln -sf /var/lib/rabbitmq/.erlang.cookie /root/ \  
&& ln -sf /usr/lib/rabbitmq/lib/rabbitmq_server-$RABBITMQ_VERSION/plugins
/plugins  
  
  
ENV RABBITMQ_LOGS=- RABBITMQ_SASL_LOGS=- PATH=/usr/lib/rabbitmq/bin:$PATH
HOME=/var/lib/rabbitmq  
# https://github.com/rabbitmq/rabbitmq-
server/commit/53af45bf9a162dec849407d114041aad3d84feaf  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY haproxy.cfg /etc/haproxy.cfg  
COPY scripts /scripts  
  
RUN set -ex \  
&& mkdir -p /var/log/supervisor \  
&& chmod +x /scripts/*  
  
  
EXPOSE 4369 5671 5672 15672 25672 8080  
CMD ["/usr/bin/supervisord"]

