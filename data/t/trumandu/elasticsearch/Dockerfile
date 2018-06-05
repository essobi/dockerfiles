FROM openjdk:8-jre-alpine  
  
# ensure elasticsearch user exists  
RUN addgroup -S elasticsearch && adduser -S -G elasticsearch elasticsearch  
  
# grab su-exec for easy step-down from root  
# and bash for "bin/elasticsearch" among others  
RUN apk add --no-cache 'su-exec>=0.2' bash  
  
# https://artifacts.elastic.co/GPG-KEY-elasticsearch  
ENV GPG_KEY 46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
WORKDIR /opt/app/elasticsearch  
ENV PATH /opt/app/elasticsearch/bin:$PATH  
  
ENV ELASTICSEARCH_VERSION 5.5.1  
ENV
ELASTICSEARCH_TARBALL="https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.1.tar.gz"  
  
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
chown -R elasticsearch:elasticsearch "$path"; \  
done; \  
\  
# we shouldn't need much RAM to test --version (default is 2gb, which gets
Jenkins in trouble sometimes)  
export ES_JAVA_OPTS='-Xms32m -Xmx32m'; \  
if [ "${ELASTICSEARCH_VERSION%%.*}" -gt 1 ]; then \  
elasticsearch --version; \  
else \  
# elasticsearch 1.x doesn't support --version  
# but in 5.x, "-v" is verbose (and "-V" is --version)  
elasticsearch -v; \  
fi  
  
COPY config ./config  
  
VOLUME /opt/app/elasticsearch/data  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 9200 9300  
#ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["elasticsearch"]  

