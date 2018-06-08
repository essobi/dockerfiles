FROM alpine:latest  
MAINTAINER Shota Kondo <der.passant.b@gmail.com>  
  
ENV PRESTO_VERSION 0.189  
RUN apk add --no-cache --virtual .fetch-deps \  
curl \  
tar \  
&& apk add --no-cache --virtual .run-deps \  
util-linux \  
less \  
openjdk8-jre \  
python \  
&& mkdir -p /opt/presto/etc \  
&& mkdir -p /var/presto/data \  
&& curl https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/${PRESTO_VERSION}/presto-server-${PRESTO_VERSION}.tar.gz | \  
tar -xz -C /opt/presto --strip-components 1 \  
&& chmod +x /opt/presto/bin/launcher \  
&& mkdir -p /usr/local/bin \  
&& curl -o /usr/local/bin/presto-cli \  
https://repo1.maven.org/maven2/com/facebook/presto/presto-
cli/${PRESTO_VERSION}/presto-cli-${PRESTO_VERSION}-executable.jar \  
&& chmod +x /usr/local/bin/presto-cli \  
&& apk del .fetch-deps  
  
EXPOSE 8080  
VOLUME /var/presto/data  
COPY ./files /opt/gen_config  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/opt/presto/bin/launcher", "run"]  

