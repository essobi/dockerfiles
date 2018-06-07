FROM muicoder/glibc:server-jre  
  
ARG ELASTICSEARCH_VERSION=6.0.0  
ARG
ELASTICSEARCH_TARBALL=https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz  
ARG ELASTICSEARCH_GPG_KEY=46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ARG WORK=/usr/share/elasticsearch  
ENV PATH=$WORK/bin:$PATH  
  
WORKDIR $WORK  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps \  
gnupg \  
openssl \  
; gpg_verify () { file=$1;url=$2;url_asc=$3;gpg_key=$4;wget -qO "$file"
"$url";if [ "$url_asc" ]; then wget -qO "$file".asc "$url_asc";export
GNUPGHOME="$(mktemp -d)";gpg --keyserver ha.pool.sks-keyservers.net --recv-
keys "$gpg_key";gpg --batch --verify "$file".asc "$file";rm -rf "$GNUPGHOME"
"$file".asc;fi;}; \  
if $(gpg_verify elasticsearch.tar.gz "$ELASTICSEARCH_TARBALL"
"$ELASTICSEARCH_TARBALL".asc $"ELASTICSEARCH_GPG_KEY"); then \  
tar -xf elasticsearch.tar.gz --strip-components=1 && rm elasticsearch.tar.gz;
\  
fi; \  
apk del .fetch-deps; \  
addgroup -S elasticsearch && adduser -S -G elasticsearch elasticsearch ; \  
chown -R elasticsearch:elasticsearch "$WORK"; \  
wget -q https://github.com/muicoder/elk/raw/master/elasticsearch/entrypoint -O
/sbin/entrypoint && chmod +x /sbin/entrypoint ; \  
elasticsearch -V && true  
  
VOLUME $WORK/data  
  
EXPOSE 9200 9300  
ENTRYPOINT ["entrypoint"]  
CMD ["elasticsearch"]  

