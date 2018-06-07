FROM insideo/jre8:8u152  
MAINTAINER ccondit@randomcoder.com  
  
RUN \  
opkg update && \  
opkg install zookeeper runas && \  
opkg clean && \  
addgroup -S -g 102 zookeeper && \  
mkdir -p /var/lib/zookeeper && \  
adduser -h /var/lib/zookeeper -g "Zookeeper user" -s /bin/sh -G zookeeper -S
-D -u 102 zookeeper && \  
chown -R zookeeper:zookeeper /var/lib/zookeeper && \  
mkdir -p /docker-entrypoint-init.d  
  
COPY docker-entrypoint.sh /  
  
ENV ZOOKEEPER_DATA_DIR /data  
ENV ZOOKEEPER_LOG_DIR /logs  
  
VOLUME /data  
VOLUME /logs  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 2181  
  
CMD [ "/usr/share/zookeeper/bin/zkServer.sh", "start-foreground" ]  

