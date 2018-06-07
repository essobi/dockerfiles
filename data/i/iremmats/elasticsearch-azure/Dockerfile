FROM docker.elastic.co/elasticsearch/elasticsearch-alpine-base:latest  
MAINTAINER Elastic Docker Team <docker@elastic.co>  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
WORKDIR /usr/share/elasticsearch  
  
# Download/extract defined ES version. busybox tar can't strip leading dir.  
RUN wget
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.0.2.tar.gz
&& \  
EXPECTED_SHA=$(wget -O -
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.0.2.tar.gz.sha1)
&& \  
test $EXPECTED_SHA == $(sha1sum elasticsearch-5.0.2.tar.gz | awk '{print $1}')
&& \  
tar zxf elasticsearch-5.0.2.tar.gz && \  
chown -R elasticsearch:elasticsearch elasticsearch-5.0.2 && \  
mv elasticsearch-5.0.2/* . && \  
rmdir elasticsearch-5.0.2 && \  
rm elasticsearch-5.0.2.tar.gz  
  
RUN set -ex && for esdirs in config data logs; do \  
mkdir -p "$esdirs"; \  
chown -R elasticsearch:elasticsearch "$esdirs"; \  
done  
  
USER elasticsearch  
  
# Install xpack and azure repository plugin  
RUN eval elasticsearch-plugin install --batch x-pack  
RUN bin/elasticsearch-plugin install repository-azure  
  
COPY elasticsearch.yml config/  
COPY log4j2.properties config/  
COPY bin/es-docker bin/es-docker  
  
USER root  
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml
config/log4j2.properties bin/es-docker && \  
chmod 0750 bin/es-docker  
  
USER elasticsearch  
CMD ["/bin/bash", "bin/es-docker"]  
  
EXPOSE 9200 9300

