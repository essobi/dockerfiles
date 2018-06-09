FROM ubuntu:16.04  
  
ENV ELASTICSEARCH_VERSION=5.0.0 GOSU_VERSION=1.9 CASSANDRA_VERSION=3.7
RBEE_AUTOKILL=true RBEE_MASTER_HOST=tasks.rbee-mlog-master
JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
RUN set -x \  
# Update cache  
&& apt-get update \  
  
# Update base image (security updates)  
# && apt-get upgrade -y \  
  
# Install step #1. Some requirements for other installations  
&& apt-get install -y \--no-install-recommends supervisor apt-transport-https
software-properties-common ca-certificates wget curl iproute \  
  
# Manually add users  
&& groupadd -r cassandra \--gid=999 && useradd -r -g cassandra --uid=999
cassandra \  
&& groupadd -r elasticsearch \--gid=998 && useradd -r -g elasticsearch
--uid=998 elasticsearch \  
  
# grab gosu for easy step-down from root  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
  
# Add GPG keys, add repos, update and install Cassandra and Elasticsearch and
Oracle Java  
# https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-
repositories.html  
&& apt-key adv \--keyserver ha.pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4 \  
&& apt-key adv \--keyserver ha.pool.sks-keyservers.net --recv-keys
514A2AD631A57A16DD0047EC749D6EEC0353B12C \  
  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
  
&& echo "deb http://www.apache.org/dist/cassandra/debian 37x main" >
/etc/apt/sources.list.d/cassandra.list \  
&& echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" >
/etc/apt/sources.list.d/elasticsearch.list \  
  
&& apt-get update && apt-get install -y \--no-install-recommends oracle-
java8-installer elasticsearch="$ELASTICSEARCH_VERSION"
cassandra="$CASSANDRA_VERSION" \  
  
&& apt-get purge -y \--auto-remove apt-transport-https software-properties-
common \  
&& rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/oracle-jdk8-installer  
  
VOLUME /usr/share/elasticsearch/data /var/lib/cassandra  
  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY scripts /scripts  
  
COPY config /usr/share/elasticsearch/config  
  
RUN set -ex \  
&& for path in \  
/usr/share/elasticsearch/data \  
/usr/share/elasticsearch/logs \  
/usr/share/elasticsearch/config \  
/usr/share/elasticsearch/config/scripts \  
; do \  
mkdir -p "$path"; \  
chown -R elasticsearch:elasticsearch "$path"; \  
done \  
&& chown -R cassandra:cassandra /etc/cassandra /var/lib/cassandra \  
&& chmod +x /scripts/* \  
&& mkdir -p /var/log/supervisor \  
&& sed -i "s/# cluster\\.name:.*/cluster\\.name: rbee-mlog/g"
/etc/elasticsearch/elasticsearch.yml \  
&& sed -i "s/cluster_name:.*/cluster_name: 'rbee-mlog'/g"
/etc/cassandra/cassandra.yaml  
  
EXPOSE 9200 9300 9042 9160  
CMD ["/usr/bin/supervisord"]

