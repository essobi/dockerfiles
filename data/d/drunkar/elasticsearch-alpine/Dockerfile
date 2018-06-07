FROM alpine:3.4  
MAINTAINER Drunkar <drunkars.p@gmail.com>  
  
  
  
##############################################################################  
# timezone: tokyo  
##############################################################################  
RUN apk --update add tzdata && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
  
##############################################################################  
# openjdk 8-jre  
##############################################################################  
ENV LANG C.UTF-8  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u111  
ENV JAVA_ALPINE_VERSION 8.111.14-r0  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
  
  
##############################################################################  
# elasticsearch 5  
##############################################################################  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN apk --no-cache add curl && \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" &&
\  
chmod +x /usr/local/bin/gosu && gosu nobody true  
  
  
ENV ELASTICSEARCH_VERSION 5.0.2  
  
RUN curl
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz
-o elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && \  
tar -xzf elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && rm
elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && \  
mv elasticsearch-$ELASTICSEARCH_VERSION /usr/share/elasticsearch  
  
RUN adduser -DH -s /sbin/nologin elasticsearch && \  
chown -R elasticsearch:elasticsearch /usr/share/elasticsearch && \  
# We replace the banshee to sh since there is no bash in base alpine linux  
sed -i -e '1 s?^#!/bin/bash?#!/bin/sh?g'
/usr/share/elasticsearch/bin/elasticsearch  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
WORKDIR /usr/share/elasticsearch  
  
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
COPY docker-entrypoint.sh /  
RUN chown elasticsearch:elasticsearch /docker-entrypoint.sh  
  
VOLUME /usr/share/elasticsearch/data  
  
EXPOSE 9200 9300  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["elasticsearch"]  

