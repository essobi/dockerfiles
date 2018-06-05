FROM openjdk:8u111-jre-alpine  
  
ARG MIRROR=http://mirror.vorboss.net/apache  
ARG VERSION=3.4.8  
ARG SIGN=http://www-eu.apache.org/dist  
  
LABEL name="zookeeper" version=$VERSION  
  
WORKDIR /opt/zookeeper  
  
RUN addgroup -S zookeeper && adduser -S -G zookeeper zookeeper  
  
RUN set -ex \  
&& apk update \  
&& apk add --no-cache wget bash gnupg su-exec \  
&& apk add --upgrade tar \  
&& wget -q $SIGN/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz.asc \  
&& wget -q --show-progress --progress=bar:force
$MIRROR/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz \  
&& wget -q -O - http://www-eu.apache.org/dist/zookeeper/KEYS | gpg --import \  
&& gpg --verify zookeeper-$VERSION.tar.gz.asc \  
&& tar -zxf zookeeper-$VERSION.tar.gz --strip=1 \  
&& rm zookeeper-$VERSION.tar.gz* \  
&& apk del wget gnupg \  
&& rm -rf /var/cache/apk/* \i  
  
RUN set -ex \  
&& echo "tickTime=2000" > conf/zoo.cfg \  
&& echo "dataDir=/opt/zookeeper/data" >> conf/zoo.cfg \  
&& echo "dataLogDir=/opt/zookeeper/data-log" >> conf/zoo.cfg \  
&& echo "clientPort=2181" >> conf/zoo.cfg  
  
RUN set -x \  
&& mkdir data-log && chown zookeeper:zookeeper data-log \  
&& mkdir data && chown zookeeper:zookeeper data \  
&& chown -R zookeeper:zookeeper conf  
  
VOLUME ["/opt/zookeeper/conf", "/opt/zookeeper/data", "/opt/zookeeper/data-
log"]  
  
EXPOSE 2181 2888 3888  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["start-foreground"]  

