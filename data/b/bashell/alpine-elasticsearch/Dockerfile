FROM bashell/alpine-bash  
  
# update/upgrade everything  
RUN apk update && apk upgrade  
  
# install jre & openssl  
RUN apk add openjdk8-jre openssl coreutils  
  
# grab gosu for easy step-down from root  
ENV GOSU_BASE https://github.com/tianon/gosu/releases/download  
ENV GOSU_VERSION 1.10  
RUN set -x \  
&& apk add gnupg \  
&& wget -O /usr/local/bin/gosu "$GOSU_BASE/$GOSU_VERSION/gosu-$(apk --print-
arch |sed -e 's/x86_64/amd64/')" \  
&& wget -O /usr/local/bin/gosu.asc "$GOSU_BASE/$GOSU_VERSION/gosu-$(apk
--print-arch |sed -e 's/x86_64/amd64/').asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg2 --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg2 --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apk del gnupg  
  
ENV VERSION 6.2.1  
ENV DOWNLOAD_URL https://artifacts.elastic.co/downloads/elasticsearch  
RUN mkdir -p /opt && adduser -h /opt/elasticsearch -g elasticsearch -s
/bin/bash -D elasticsearch  
  
WORKDIR /opt  
RUN ln -s elasticsearch elasticsearch-$VERSION  
USER elasticsearch  
RUN set -x \  
&& wget -O - "$DOWNLOAD_URL/elasticsearch-$VERSION.tar.gz" | tar zxvf -  
  
ENV PATH /opt/elasticsearch/bin:$PATH  
  
WORKDIR /opt/elasticsearch  
RUN set -ex \  
&& for path in \  
./data \  
./logs \  
./config \  
./config/scripts \  
; do \  
mkdir -p "$path"; \  
chown -R elasticsearch:elasticsearch "$path"; \  
done  
  
COPY config ./config  
  
VOLUME /opt/elasticsearch/data  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 9200 9300  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["elasticsearch"]  
  

