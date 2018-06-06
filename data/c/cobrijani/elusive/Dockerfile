FROM phusion/baseimage  
  
LABEL maintainer "Stefan Bratic <cobrijani@gmail.com>"  
  
###############################################################################  
# INSTALLATION  
###############################################################################  
  
### install prerequisites (cURL, gosu, JDK)  
  
ENV GOSU_VERSION 1.8  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qqy --no-install-recommends ca-certificates curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -L -o /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -L -o /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get update -qq \  
&& apt-get install -qqy openjdk-8-jdk \  
&& apt-get clean \  
&& set +x  
  
  
ENV ELK_VERSION 5.4.1  
  
### install Elasticsearch  
  
ENV ES_VERSION ${ELK_VERSION}  
ENV ES_HOME /opt/elasticsearch  
ENV ES_PACKAGE elasticsearch-${ES_VERSION}.tar.gz  
ENV ES_GID 991  
ENV ES_UID 991  
  
RUN mkdir ${ES_HOME} \  
&& curl -O https://artifacts.elastic.co/downloads/elasticsearch/${ES_PACKAGE}
\  
&& tar xzf ${ES_PACKAGE} -C ${ES_HOME} --strip-components=1 \  
&& rm -f ${ES_PACKAGE} \  
&& groupadd -r elasticsearch -g ${ES_GID} \  
&& useradd -r -s /usr/sbin/nologin -M -c "Elasticsearch service user" -u
${ES_UID} -g elasticsearch elasticsearch \  
&& mkdir -p /var/log/elasticsearch /etc/elasticsearch
/etc/elasticsearch/scripts /var/lib/elasticsearch \  
&& chown -R elasticsearch:elasticsearch ${ES_HOME} /var/log/elasticsearch
/var/lib/elasticsearch \  
&& .${ES_HOME}/bin/elasticsearch-plugin install --batch x-pack \  
&& .${ES_HOME}/bin/elasticsearch-plugin install ingest-user-agent \  
&& .${ES_HOME}/bin/elasticsearch-plugin install ingest-geoip  
  
  
ADD ./elasticsearch-init /etc/init.d/elasticsearch  
RUN sed -i -e 's#^ES_HOME=$#ES_HOME='$ES_HOME'#' /etc/init.d/elasticsearch \  
&& chmod +x /etc/init.d/elasticsearch  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
  
### configure Elasticsearch  
  
ADD ./elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
ADD ./elasticsearch-log4j2.properties /etc/elasticsearch/log4j2.properties  
ADD ./elasticsearch-jvm.options /etc/elasticsearch/jvm.options  
ADD ./elasticsearch-default /etc/default/elasticsearch  
  
RUN mkdir /etc/elasticsearch/ingest-geoip \  
&& chmod -R +r /etc/elasticsearch  
  
### configure logrotate  
ADD ./elasticsearch-logrotate /etc/logrotate.d/elasticsearch  
RUN chmod 644 /etc/logrotate.d/elasticsearch  
  
  
ENV ES_CONFIG=/etc/elasticsearch  
ENV X_PACK_ES=${ES_CONFIG}/x-pack  
  
  
ADD ./cryptography/certs/ca/ca.pem ${X_PACK_ES}/ca.pem  
ADD ./cryptography/certs/ca/ca.key ${X_PACK_ES}/ca.key  
ADD ./cryptography/certs/elusive-1/elusive-1.pem ${X_PACK_ES}/elusive-1.pem  
ADD ./cryptography/certs/elusive-1/elusive-1.key ${X_PACK_ES}/elusive-1.key  
ADD ./cryptography/jks/elasticsearch-keystore.jks ${X_PACK_ES}/elasticsearch-
keystore.jks  
ADD ./cryptography/jks/elasticsearch-truststore.jks
${X_PACK_ES}/elasticsearch-truststore.jks  
ADD role_mapping.yml ${X_PACK_ES}/role_mapping.yml  
  
  
###############################################################################  
# START  
###############################################################################  
  
ADD ./start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
EXPOSE 9200 9300  
VOLUME /var/lib/elasticsearch  
  
CMD [ "/usr/local/bin/start.sh" ]  

