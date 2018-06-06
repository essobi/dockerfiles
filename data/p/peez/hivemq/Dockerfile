FROM alpine:3.7  
LABEL maintainer="peez@stiffi.de"  
RUN apk add \--no-cache bash openjdk8-jre ca-certificates wget \  
&& update-ca-certificates  
  
COPY docker-install-scripts/ /docker-install-scripts/  
RUN source /docker-install-scripts/install_hivemq.sh  
RUN source /docker-install-scripts/install_auth_plugin.sh  
RUN source /docker-install-scripts/install_graphite_plugin.sh  
RUN source /docker-install-scripts/install_database_cluster_plugin.sh  
  
# Since /opt overwrites some default files that are created upon hivemq
installation, this COPY command has to be done AFTER the install-scripts  
COPY opt/ /opt/  
RUN chown -R hivemq:hivemq /opt \  
&& chmod +x /opt/docker-entrypoint.sh  
  
  
ENV \  
HIVEMQ_KEYSTORE_PASSWORD="password" \  
HIVEMQ_PRIVATE_KEY_PASSWORD="password" \  
HIVEMQ_TRUSTSTORE_PASSWORD="password" \  
HIVEMQ_TLS_CLIENT_AUTHENTICATION_MODE="NONE" \  
HIVEMQ_TCP_PORT="1883" \  
HIVEMQ_TCP_TLS_PORT="8883" \  
HIVEMQ_WEBSOCKET_PORT="8000" \  
HIVEMQ_WEBSOCKET_TLS_PORT="8001" \  
HIVEMQ_PERSISTENCE_MODE="in-memory"  
# HIVEMQ_CLUSTER_JDBC_URL HIVEMQ_CLUSTER_JDBC_USER
HIVEMQ_CLUSTER_JDBC_PASSWORD  
  
  
EXPOSE $HIVEMQ_TCP_PORT $HIVEMQ_TCP_TLS_PORT $HIVEMQ_WEBSOCKET_PORT
$HIVEMQ_WEBSOCKET_TLS_PORT 7800 7900 8555 15000  
  
USER hivemq  
CMD ["/opt/docker-entrypoint.sh"]  

