FROM stakater/java8-alpine:1.8.0_121  
LABEL authors="Hazim <hazim_malik@hotmail.com>"  
# grab su-exec for easy step-down from root  
# and bash for "bin/elasticsearch" among others  
RUN apk add --no-cache 'su-exec>=0.2' bash  
  
# https://artifacts.elastic.co/GPG-KEY-elasticsearch  
ENV GPG_KEY 46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
WORKDIR /usr/share/elasticsearch  
ENV PATH /usr/share/elasticsearch/bin:$PATH \  
ES_JAVA_OPTS "-Xms1g -Xmx1g"  
  
ARG ELASTICSEARCH_VERSION=5.2.1  
ENV
ELASTICSEARCH_TARBALL="https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz"
\  
ELASTICSEARCH_TARBALL_ASC="https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz.asc"
\  
ELASTICSEARCH_TARBALL_SHA1="93bae92937075fed18ac4a4dd57798aca792af03"  
  
RUN set -ex; \  
\  
apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
gnupg \  
openssl \  
tar \  
; \  
\  
wget -O elasticsearch.tar.gz "$ELASTICSEARCH_TARBALL"; \  
\  
if [ "$ELASTICSEARCH_TARBALL_SHA1" ]; then \  
echo "$ELASTICSEARCH_TARBALL_SHA1 *elasticsearch.tar.gz" | sha1sum -c -; \  
fi; \  
\  
if [ "$ELASTICSEARCH_TARBALL_ASC" ]; then \  
wget -O elasticsearch.tar.gz.asc "$ELASTICSEARCH_TARBALL_ASC"; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY"; \  
gpg --batch --verify elasticsearch.tar.gz.asc elasticsearch.tar.gz; \  
rm -r "$GNUPGHOME" elasticsearch.tar.gz.asc; \  
fi; \  
\  
tar -xf elasticsearch.tar.gz --strip-components=1; \  
rm elasticsearch.tar.gz; \  
\  
apk del .fetch-deps; \  
\  
mkdir -p ./plugins; \  
for path in \  
./data \  
./logs \  
./config \  
./config/scripts \  
; do \  
mkdir -p "$path"; \  
chown -R stakater:stakater "$path"; \  
done; \  
\  
if [ "${ELASTICSEARCH_VERSION%%.*}" -gt 1 ]; then \  
elasticsearch --version; \  
else \  
# elasticsearch 1.x doesn't support --version  
# but in 5.x, "-v" is verbose (and "-V" is --version)  
elasticsearch -v; \  
fi  
  
COPY config ./config  
  
VOLUME /usr/share/elasticsearch/data  
  
EXPOSE 9200 9300  
# Simulate cmd behavior via environment variable  
# So that users are able to provice command line arguments to elastic search  
ENV COMMAND "elasticsearch"  
# Make daemon service dir for logstash and place file  
# It will be started and maintained by the base image  
RUN mkdir -p /etc/service/elasticsearch  
ADD start.sh /etc/service/elasticsearch/run  
  
# Use base image's entrypoint

