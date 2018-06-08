FROM ubuntu:16.04  
MAINTAINER pastakhov@yandex.ru  
  
# Install requered packages  
RUN set -x; \  
apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ca-certificates \  
default-jre \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apt/archives/*  
  
ENV VERSION=2.4.5 \  
ES_USER=elasticsearch \  
ES_HOME=/usr/share/elasticsearch \  
ES_VOLUME=/elasticsearch \  
ES_JAVA_OPTS=-Xms512m\ -Xmx512m \  
ES_LOGGER_LEVEL=INFO  
  
RUN set -x; \  
mkdir -p $ES_HOME \  
&& wget -qO-
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/${VERSION}/elasticsearch-${VERSION}.tar.gz
| tar xvz -C $ES_HOME \--strip 1 \  
&& mkdir -p $ES_VOLUME/data \  
&& mkdir -p $ES_VOLUME/logs \  
&& mkdir -p $ES_HOME/plugins \  
&& mkdir -p $ES_HOME/config/scripts \  
&& useradd -U -r -s /bin/bash $ES_USER  
  
EXPOSE 9200  
#HEALTHCHECK --timeout=5s CMD wget -q -O - http://$HOSTNAME:9200/_cat/health  
VOLUME $ES_VOLUME  
  
COPY run-elasticsearch.sh /run-elasticsearch.sh  
RUN chmod -v +x /run-elasticsearch.sh  
  
CMD ["/run-elasticsearch.sh"]  

