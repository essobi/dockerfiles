# Dockerfile for Elasticsearch  
  
# Build with:  
# docker build -t <repo-user>/elasticsearch .  
  
# Run with:  
# docker run -p 9200:9200 -p 9300:9300 -it --name elasticsearch <repo-
user>/elasticsearch  
  
FROM phusion/baseimage  
MAINTAINER paladintyrion <paladintyrion@gmail.com>  
  
###############################################################################  
# GROUP && USER  
###############################################################################  
  
ENV ES_HOME /opt/elasticsearch  
# ensure logstash user exists  
ENV ES_GID 441  
ENV ES_UID 441  
  
RUN groupadd -r elasticsearch -g ${ES_GID} \  
&& useradd -r -s /usr/sbin/nologin -M -c "Elasticsearch service user" -u
${ES_UID} -g elasticsearch elasticsearch  
  
###############################################################################  
# GOSU && TIMEZONE && JDK8  
###############################################################################  
  
ENV GOSU_VERSION 1.10  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -yq --no-install-recommends tzdata cron \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get install -qqy --no-install-recommends ca-certificates wget curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture | awk -F- '{ print $NF }').asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get update -qq \  
&& apt-get install -qqy openjdk-8-jdk \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& apt-get clean \  
&& rm -fr /tmp/* \  
&& set +x  
  
###############################################################################  
# INSTALL ELASTICSEARCH  
###############################################################################  
  
# COPY ./limits.conf /etc/security/limits.conf  
# RUN chmod +r /etc/security/limits.conf  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV ES_PATH $ES_HOME/bin  
ENV PATH $ES_PATH:$PATH  
  
RUN mkdir -p ${ES_HOME} \  
&& mkdir -p /var/log/elasticsearch /etc/elasticsearch
/etc/elasticsearch/scripts /var/lib/elasticsearch /tmp/elasticsearch \  
&& chown -R elasticsearch:elasticsearch ${ES_HOME} /var/log/elasticsearch
/var/lib/elasticsearch /etc/elasticsearch /tmp/elasticsearch \  
&& mkdir -p /etc/logrotate.d  
  
### install Elasticsearch  
  
ENV ES_VERSION 5.6.3  
ENV ES_PACKAGE elasticsearch-${ES_VERSION}.tar.gz  
  
RUN curl -O https://artifacts.elastic.co/downloads/elasticsearch/${ES_PACKAGE}
\  
&& tar -xzf ${ES_PACKAGE} -C ${ES_HOME} --strip-components=1 \  
&& rm -f ${ES_PACKAGE} \  
&& apt-get autoremove \  
&& apt-get autoclean  
  
COPY ./elasticsearch-init /etc/init.d/elasticsearch  
RUN sed -i -e 's#^ES_HOME=$#ES_HOME='$ES_HOME'#' /etc/init.d/elasticsearch \  
&& chmod +x /etc/init.d/elasticsearch  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
  
### configure Elasticsearch  
  
COPY ./elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
COPY ./elasticsearch-log4j2.properties /etc/elasticsearch/log4j2.properties  
COPY ./elasticsearch-jvm.options /opt/elasticsearch/config/jvm.options  
COPY ./elasticsearch-default /etc/default/elasticsearch  
RUN chmod -R +r /etc/elasticsearch  
  
### configure logrotate  
  
COPY ./elasticsearch-logrotate /etc/logrotate.d/elasticsearch  
RUN chmod 644 /etc/logrotate.d/elasticsearch  
  
###############################################################################  
# PREPARE START  
###############################################################################  
  
COPY ./replace_ips.sh /usr/local/bin/replace_ips.sh  
COPY ./start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/replace_ips.sh \  
&& chmod +x /usr/local/bin/start.sh  
  
  
###############################################################################  
# XPACK INSTALLATION  
###############################################################################  
  
# ENV XPACK_VERSION 5.6.3  
# ENV XPACK_PACKAGE x-pack-${XPACK_VERSION}.zip  
#  
# WORKDIR /tmp  
# RUN curl -O
https://artifacts.elastic.co/downloads/packs/x-pack/${XPACK_PACKAGE} \  
# && gosu elasticsearch ${ES_HOME}/bin/elasticsearch-plugin install \  
# -Edefault.path.conf=/etc/elasticsearch \  
# --batch file:///tmp/${XPACK_PACKAGE} \  
# && gosu kibana ${KIBANA_HOME}/bin/kibana-plugin install \  
# file:///tmp/${XPACK_PACKAGE} \  
# && rm -f ${XPACK_PACKAGE}  
#  
# RUN sed -i -e 's/curl localhost:9200/curl -u elastic:changeme
localhost:9200/' \  
# -e 's/curl localhost:5601/curl -u kibana:paladin localhost:5601/' \  
# /usr/local/bin/start.sh  
  
###############################################################################  
# START  
###############################################################################  
  
EXPOSE 9200 9300  
VOLUME ["/var/lib/elasticsearch"]  
  
ENTRYPOINT [ "/usr/local/bin/start.sh", "$@" ]  

