# Docker file to create Elasticsearch container.  
FROM cgswong/java:openjre8  
MAINTAINER Stuart Wong <cgs.wong@gmail.com>  
  
# Setup environment  
ENV ES_VERSION 1.7.3  
ENV ES_PLUGIN_AWS_VERSION 2.7.1  
ENV ES_PLUGIN_BIGDESK_VERSION 2.5.0  
ENV ES_PLUGIN_WHATSON_VERSION 0.1.3  
ENV ES_PLUGIN_KOPF_VERSION 1.0  
ENV ES_HOME /opt/elasticsearch  
ENV ES_VOL /var/lib/elasticsearch  
ENV ES_USER elasticsearch  
ENV ES_GROUP elasticsearch  
  
# Install requirements and Elasticsearch  
RUN apk --update add \  
curl \  
python \  
py-pip \  
bash && \  
mkdir -p \  
${ES_VOL}/data \  
${ES_VOL}/logs \  
${ES_VOL}/plugins \  
${ES_VOL}/work \  
${ES_VOL}/config \  
/opt &&\  
curl -sSL
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz
| tar zxf - -C /opt &&\  
ln -s /opt/elasticsearch-${ES_VERSION} ${ES_HOME} &&\  
addgroup ${ES_GROUP} &&\  
adduser -h ${ES_HOME} -D -s /bin/bash -G ${ES_GROUP} ${ES_USER} &&\  
chown -R ${ES_USER}:${ES_GROUP} ${ES_HOME}/ ${ES_VOL} &&\  
${ES_HOME}/bin/plugin -install elasticsearch/elasticsearch-cloud-
aws/${ES_PLUGIN_AWS_VERSION} \--silent --timeout 2m &&\  
${ES_HOME}/bin/plugin -install lukas-
vlcek/bigdesk/${ES_PLUGIN_BIGDESK_VERSION} \--silent --timeout 2m &&\  
${ES_HOME}/bin/plugin -install xyu/elasticsearch-
whatson/${ES_PLUGIN_WHATSON_VERSION} \--silent --timeout 2m &&\  
${ES_HOME}/bin/plugin -install lmenezes/elasticsearch-
kopf/${ES_PLUGIN_KOPF_VERSION} \--silent --timeout 2m &&\  
${ES_HOME}/bin/plugin -install royrusso/elasticsearch-HQ --silent --timeout 2m  
  
# Configure environment  
COPY src/ /  
  
# Expose volumes  
VOLUME ["${ES_VOL}"]  
  
# Define working directory.  
WORKDIR ${ES_VOL}  
  
# Listen for 9200/tcp (HTTP) and 9300/tcp (cluster)  
EXPOSE 9200 9300  
# Start container  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD [""]  

