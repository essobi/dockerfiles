FROM phusion/baseimage  
MAINTAINER Maestrano <it@maestrano.com>  
  
#=============================================  
# INSTALLATION  
#=============================================  
ENV GOSU_VERSION 1.8  
ENV ELK_VERSION 5.4.0  
ENV LOGSTASH_VERSION ${ELK_VERSION}  
ENV KIBANA_VERSION ${ELK_VERSION}  
ENV XPACK_VERSION ${ELK_VERSION}  
ENV ES_CURATOR_VERSION 5.2.0  
### Install prerequisites (cURL, gosu, JDK, pip)  
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
&& apt-get install -qqy openjdk-8-jdk python-pip \  
&& apt-get clean \  
&& set +x  
  
### Install Elasticsearch  
ENV ES_VERSION ${ELK_VERSION}  
ENV ES_HOME /opt/elasticsearch  
ENV ES_PACKAGE elasticsearch-${ES_VERSION}.tar.gz  
ENV ES_GID 991  
ENV ES_UID 991  
RUN mkdir ${ES_HOME} \  
&& curl -O https://artifacts.elastic.co/downloads/elasticsearch/${ES_PACKAGE}
\  
&& tar xzf ${ES_PACKAGE} -C ${ES_HOME} \--strip-components=1 \  
&& rm -f ${ES_PACKAGE} \  
&& groupadd -r elasticsearch -g ${ES_GID} \  
&& useradd -r -s /usr/sbin/nologin -M -c "Elasticsearch service user" -u
${ES_UID} -g elasticsearch elasticsearch \  
&& mkdir -p /var/log/elasticsearch /etc/elasticsearch
/etc/elasticsearch/scripts /var/lib/elasticsearch \  
&& chown -R elasticsearch:elasticsearch ${ES_HOME} /var/log/elasticsearch
/var/lib/elasticsearch  
  
COPY elasticsearch/elasticsearch.init /etc/init.d/elasticsearch  
RUN sed -i -e 's#^ES_HOME=$#ES_HOME='$ES_HOME'#' /etc/init.d/elasticsearch \  
&& chmod +x /etc/init.d/elasticsearch  
  
### Install Elasticsearch Curator  
RUN pip install elasticsearch-curator==${ES_CURATOR_VERSION}  
  
### Install Logstash  
ENV LOGSTASH_HOME /opt/logstash  
ENV LOGSTASH_PACKAGE logstash-${LOGSTASH_VERSION}.tar.gz  
ENV LOGSTASH_GID 992  
ENV LOGSTASH_UID 992  
RUN mkdir ${LOGSTASH_HOME} \  
&& curl -O https://artifacts.elastic.co/downloads/logstash/${LOGSTASH_PACKAGE}
\  
&& tar xzf ${LOGSTASH_PACKAGE} -C ${LOGSTASH_HOME} \--strip-components=1 \  
&& rm -f ${LOGSTASH_PACKAGE} \  
&& groupadd -r logstash -g ${LOGSTASH_GID} \  
&& useradd -r -s /usr/sbin/nologin -d ${LOGSTASH_HOME} -c "Logstash service
user" -u ${LOGSTASH_UID} -g logstash logstash \  
&& mkdir -p /var/log/logstash /etc/logstash/conf.d \  
&& chown -R logstash:logstash ${LOGSTASH_HOME} /var/log/logstash  
  
COPY logstash/logstash.init /etc/init.d/logstash  
RUN sed -i -e 's#^LS_HOME=$#LS_HOME='$LOGSTASH_HOME'#' /etc/init.d/logstash \  
&& chmod +x /etc/init.d/logstash  
  
### Install Kibana  
ENV KIBANA_HOME /opt/kibana  
ENV KIBANA_PACKAGE kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz  
ENV KIBANA_GID 993  
ENV KIBANA_UID 993  
RUN mkdir ${KIBANA_HOME} \  
&& curl -O https://artifacts.elastic.co/downloads/kibana/${KIBANA_PACKAGE} \  
&& tar xzf ${KIBANA_PACKAGE} -C ${KIBANA_HOME} \--strip-components=1 \  
&& rm -f ${KIBANA_PACKAGE} \  
&& groupadd -r kibana -g ${KIBANA_GID} \  
&& useradd -r -s /usr/sbin/nologin -d ${KIBANA_HOME} -c "Kibana service user"
-u ${KIBANA_UID} -g kibana kibana \  
&& mkdir -p /var/log/kibana \  
&& chown -R kibana:kibana ${KIBANA_HOME} /var/log/kibana  
  
COPY kibana/kibana.init /etc/init.d/kibana  
RUN sed -i -e 's#^KIBANA_HOME=$#KIBANA_HOME='$KIBANA_HOME'#'
/etc/init.d/kibana \  
&& chmod +x /etc/init.d/kibana  
  
### Install XPack  
ENV XPACK_PACKAGE x-pack-${XPACK_VERSION}.zip  
  
WORKDIR /tmp  
RUN curl -O
https://artifacts.elastic.co/downloads/packs/x-pack/${XPACK_PACKAGE} \  
&& gosu elasticsearch ${ES_HOME}/bin/elasticsearch-plugin install \  
-Edefault.path.conf=/etc/elasticsearch \  
file:///tmp/${XPACK_PACKAGE} \--batch \  
&& gosu kibana ${KIBANA_HOME}/bin/kibana-plugin install \  
file:///tmp/${XPACK_PACKAGE} \  
&& gosu logstash ${LOGSTASH_HOME}/bin/logstash-plugin install \  
file:///tmp/${XPACK_PACKAGE} \  
&& rm -f ${XPACK_PACKAGE}  
  
#=============================================  
# CONFIGURATION  
#=============================================  
### Elasticsearch configuration  
COPY elasticsearch/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
COPY elasticsearch/log4j2.properties /etc/elasticsearch/log4j2.properties  
COPY elasticsearch/jvm.options /etc/elasticsearch/jvm.options  
COPY elasticsearch/elasticsearch.default /etc/default/elasticsearch  
RUN chmod -R +r /etc/elasticsearch  
  
### Elasticsearch Curator configuration  
COPY elasticsearch/curator.yml /etc/elasticsearch/curator.yml  
COPY elasticsearch/curator_action.yml /etc/elasticsearch/curator_action.yml  
COPY cron/es_curator.sh /etc/cron.daily/es_curator.sh  
RUN chmod 775 /etc/cron.daily/es_curator.sh  
  
### Logstash configuration  
# certs/keys for Beats and Lumberjack input  
RUN mkdir -p /etc/pki/tls/certs && mkdir /etc/pki/tls/private  
COPY logstash/certs/logstash-beats.crt /etc/pki/tls/certs/logstash-beats.crt  
COPY logstash/certs/logstash-beats.key /etc/pki/tls/private/logstash-beats.key  
  
# Logstash configuration  
COPY logstash/logstash.yml ${LOGSTASH_HOME}/config/logstash.yml  
  
# Logstash filters  
COPY logstash/conf.d /etc/logstash/conf.d  
  
# Logstash patterns  
COPY logstash/patterns ${LOGSTASH_HOME}/patterns  
RUN chown -R logstash:logstash ${LOGSTASH_HOME}/patterns  
  
# Logstash permissions  
RUN chmod -R +r /etc/logstash  
  
### Kibana configuration  
COPY kibana/kibana.yml ${KIBANA_HOME}/config/kibana.yml  
  
### Logrotate configuration  
COPY elasticsearch/elasticsearch.logrotate /etc/logrotate.d/elasticsearch  
COPY logstash/logstash.logrotate /etc/logrotate.d/logstash  
COPY kibana/kibana.logrotate /etc/logrotate.d/kibana  
RUN chmod 644 /etc/logrotate.d/elasticsearch \  
&& chmod 644 /etc/logrotate.d/logstash \  
&& chmod 644 /etc/logrotate.d/kibana  
  
#=============================================  
# Entrypoint  
#=============================================  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
EXPOSE 5601 9200 9300 5044  
VOLUME /var/lib/elasticsearch  
  
COPY healthcheck.sh /usr/local/bin/  
HEALTHCHECK \--timeout=5s CMD bash /usr/local/bin/healthcheck.sh  
  
CMD [ "/usr/local/bin/entrypoint.sh" ]  

