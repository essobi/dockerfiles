FROM gaven/alpine:8-jre  
  
MAINTAINER gavin-guo  
  
RUN apk add --no-cache \  
bash  
  
ENV ZOOKEEPER_VERSION=3.4.11  
ENV ZOOKEEPER_HOME="/zookeeper" \  
CODIS_HOME="/codis"  
RUN set -x \  
&& apk update \  
&& apk add --no-cache --virtual .build-deps \  
ca-certificates \  
wget \  
tar \  
&& wget -q
"http://www.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz"
\  
&& tar -xzf "zookeeper-${ZOOKEEPER_VERSION}.tar.gz" \  
&& mv "zookeeper-${ZOOKEEPER_VERSION}" "$ZOOKEEPER_HOME" \  
&& cp "$ZOOKEEPER_HOME/conf/zoo_sample.cfg" "$ZOOKEEPER_HOME/conf/zoo.cfg" \  
&& wget -q "http://sftp.chinacloudapp.cn/docker/codis3.2.2-go1.9.2-linux.zip"
\  
&& unzip codis3.2.2-go1.9.2-linux.zip \  
&& mv codis3.2.2-go1.9.2-linux "$CODIS_HOME" \  
&& rm -r "zookeeper-${ZOOKEEPER_VERSION}.tar.gz"
"codis3.2.2-go1.9.2-linux.zip" \  
&& apk del .build-deps  
  
RUN set -x \  
&& mkdir /log /template /config /scripts /data  
  
COPY template/* /template/  
COPY docker-entrypoint.sh /scripts/  
  
RUN set -x \  
&& chmod +x /scripts/*  
  
ENV PATH=$PATH:${ZOOKEEPER_HOME}/bin:${CODIS_HOME}  
  
VOLUME ["/template", "/data"]  
  
WORKDIR $CODIS_HOME  
  
EXPOSE 18090 19000 19001 19002 2181  
ENTRYPOINT ["/scripts/docker-entrypoint.sh"]

