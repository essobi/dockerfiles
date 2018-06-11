FROM cgswong/java:openjre8  
MAINTAINER Stuart Wong <cgs.wong@gmail.com>  
  
ENV ZK_VERSION 3.4.6  
ENV ZK_USER zookeeper  
ENV ZK_GROUP zookeeper  
ENV ZK_BASE_DATADIR /var/lib/zookeeper  
ENV ZK_BINDIR /opt/zookeeper  
ENV JMXPORT 12181  
COPY zkStart.sh /usr/local/bin/  
  
RUN apk --update add \  
curl \  
bash \  
tar &&\  
mkdir -p \  
${ZK_BINDIR}/conf \  
${ZK_BASE_DATADIR}/data \  
${ZK_BASE_DATADIR}/log &&\  
curl -sSL
http://mirrors.sonic.net/apache/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz
| tar zxf - -C ${ZK_BINDIR} \--strip-components=1 &&\  
addgroup ${ZK_GROUP} &&\  
adduser -h ${ZK_BASE_DATADIR} -D -s /bin/bash -G ${ZK_GROUP} ${ZK_USER} &&\  
chown -R ${ZK_USER}:${ZK_GROUP} ${ZK_BASE_DATADIR} ${ZK_BINDIR} &&\  
chmod +x /usr/local/bin/zkStart.sh  
  
COPY log4j.properties ${ZK_BINDIR}/conf/  
  
USER ${ZK_USER}  
  
# Expose client port (2188/tcp;2281/tcps), leader connection port (2888/tcp),
leader election port (3888/tcp)  
EXPOSE 2181 2281 2888 3888 ${JMXPORT}  
  
# Expose volumes  
VOLUME ["${ZK_BASE_DATADIR}","${ZK_BINDIR}/conf"]  
  
ENTRYPOINT ["/usr/local/bin/zkStart.sh"]  
CMD [""]  

