FROM jrevolt/jre  
  
ADD env.sh /  
  
RUN \  
source /env.sh && \  
NEXUS_HOME="/opt/nexus" && \  
NEXUS_DATA="/var/lib/nexus" && \  
URL="https://sonatype-
download.global.ssl.fastly.net/nexus/3/nexus-${VERSION}-unix.tar.gz" && \  
apk add --update curl && \  
mkdir -p ${NEXUS_HOME} && \  
curl -sjkL "$URL" | tar xzv -C ${NEXUS_HOME} && \  
ln -s ${NEXUS_HOME}/nexus-* ${NEXUS_HOME}/current && \  
mkdir -p ${NEXUS_DATA} && mv ${NEXUS_HOME}/sonatype-work ${NEXUS_DATA}/ && ln
-s ${NEXUS_DATA}/sonatype-work ${NEXUS_HOME}/ && \  
adduser -SD -h ${NEXUS_DATA} -G root -u 200 nexus && \  
chown -R nexus:root ${NEXUS_HOME} ${NEXUS_DATA} && \  
rm -rf /var/cache/apk/* /var/log/* /tmp/*  
  
EXPOSE 8081  
VOLUME ["/var/lib/nexus"]  
  
USER nexus  
ENTRYPOINT ["/opt/nexus/current/bin/nexus", "run"]  

