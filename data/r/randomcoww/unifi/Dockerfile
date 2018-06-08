## issues found so far..  
## - org.xerial.snappy.Snappy  
## https://community.ubnt.com/t5/UniFi-Routing-Switching/UniFi-Gateway-Cloud-
Controller/td-p/1268270/page/4  
## - ld-linux-x86-64.so.2  
## https://github.com/gliderlabs/docker-alpine/issues/219  
  
FROM openjdk:8-jre-alpine  
  
ENV UNIFI_VERSION 5.7.20  
ENV UNIFI_PATH /opt/UniFi  
  
RUN set -x \  
\  
&& apk add --no-cache --virtual .build-deps \  
unzip \  
\  
&& wget -O /tmp/unifi.zip
http://dl.ubnt.com/unifi/$UNIFI_VERSION/UniFi.unix.zip \  
&& unzip /tmp/unifi.zip -d /opt \  
&& rm /tmp/unifi.zip \  
\  
&& mkdir -p $UNIFI_PATH/data $UNIFI_PATH/logs \  
&& ln -fs /dev/stdout $UNIFI_PATH/logs/server.log \  
&& ln -fs /dev/null $UNIFI_PATH/logs/mongod.log \  
\  
&& apk add --no-cache \  
mongodb \  
libc6-compat \  
&& apk del .build-deps \  
&& rm \  
/usr/bin/mongo \  
/usr/bin/mongoperf \  
/usr/bin/mongos  
  
COPY entrypoint.sh /  
  
WORKDIR $UNIFI_PATH  
ENTRYPOINT ["/entrypoint.sh"]  

