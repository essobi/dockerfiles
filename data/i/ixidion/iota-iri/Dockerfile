FROM iotaledger/iri:v1.4.1.6 as base  
  
FROM openjdk:8-jre-slim  
  
ARG UID=1600  
ARG GID=1600  
ARG TINI_VERSION=v0.16.1  
ENV NEIGHBORS="" \  
REMOTE_API_LIMIT="attachToTangle, addNeighbors, removeNeighbors" \  
API_PORT=14265 \  
UDP_PORT=14600 \  
TCP_PORT=15600 \  
JAVA_OPTIONS="-XX:+DisableAttachMechanism -XX:+HeapDumpOnOutOfMemoryError
-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap"  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
  
COPY root /  
  
RUN chmod +x /usr/bin/tini \  
&& addgroup --gid ${GID} iota \  
&& adduser --home /opt/iri --no-create-home --uid ${UID} \--gecos "IOTA user"
\--gid ${GID} \--disabled-password iota  
  
COPY \--from=base /iri/iri.jar /opt/iri/iri.jar  
  
VOLUME /opt/iri/data  
  
EXPOSE ${API_PORT}  
EXPOSE ${UDP_PORT}/UDP  
EXPOSE ${TCP_PORT}  
  
ENTRYPOINT ["/usr/bin/tini","/docker-entrypoint.sh"]  

