FROM docker.elastic.co/elasticsearch/elasticsearch-alpine-base:latest  
MAINTAINER Elastic Docker Team <docker@elastic.co>  
  
ARG ELASTIC_VERSION=6.0.0-alpha1-SNAPSHOT  
ARG ES_DOWNLOAD_URL_PREFIX=https://snapshots.elastic.co/downloads  
ARG ES_JAVA_OPTS  
ENV
ES_DOWNLOAD_URL=${ES_DOWNLOAD_URL_PREFIX}/elasticsearch/elasticsearch-${ELASTIC_VERSION}.tar.gz  
ENV XPACK_DOWNLOAD_URL=${ES_DOWNLOAD_URL_PREFIX}/elasticsearch-
plugins/x-pack/x-pack-${ELASTIC_VERSION}.zip  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
WORKDIR /usr/share/elasticsearch  
  
RUN wget ${ES_DOWNLOAD_URL} \  
&& EXPECTED_SHA=$(wget -O - ${ES_DOWNLOAD_URL}.sha1) \  
&& test ${EXPECTED_SHA} == $(sha1sum elasticsearch-${ELASTIC_VERSION}.tar.gz |
awk '{print $1}') \  
&& tar zxf elasticsearch-${ELASTIC_VERSION}.tar.gz \  
&& chown -R elasticsearch:elasticsearch elasticsearch-${ELASTIC_VERSION} \  
&& mv elasticsearch-${ELASTIC_VERSION}/* . \  
&& rmdir elasticsearch-${ELASTIC_VERSION} \  
&& rm elasticsearch-${ELASTIC_VERSION}.tar.gz \  
&& true  
  
RUN set -ex \  
&& for esdirs in config data logs; do \  
mkdir -p "${esdirs}"; \  
chown -R elasticsearch:elasticsearch "${esdirs}"; \  
done  
  
USER elasticsearch  
  
# Install xpack  
RUN eval ${ES_JAVA_OPTS:-} elasticsearch-plugin install --batch
${XPACK_DOWNLOAD_URL}  
  
COPY elasticsearch.yml config/  
COPY log4j2.properties config/  
COPY bin/es-docker bin/es-docker  
  
USER root  
RUN chown elasticsearch:elasticsearch config/* bin/es-docker \  
&& chmod 0750 bin/es-docker  
  
USER elasticsearch  
CMD ["/bin/bash", "bin/es-docker"]  
  
EXPOSE 9200 9300  

