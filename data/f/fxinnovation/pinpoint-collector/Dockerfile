FROM tomcat:8.5.15-jre8-alpine  
  
ENV PINPOINTCOLLECTOR_VERSION=1.6.2 \  
CONFD_VERSION=0.11.0 \  
HBASE_CLIENT_HOST=localhost \  
HBASE_CLIENT_PORT=2181 \  
HBASE_ZOOKEEPER_ZNODE_PARENT="/hbase" \  
HBASE_IPC_CLIENT_TCPNODEDELAY="true" \  
HBASE_RPC_TIMEOUT=10000 \  
HBASE_CLIENT_OPERATION_TIMEOUT=10000 \  
HBASE_IPC_CLIENT_SOCKET_TIMEOUT_READ=20000 \  
HBASE_IPC_CLIENT_SOCKET_TIMEOUT_WRITE=60000 \  
HBASE_CLIENT_THREAD_MAX=64 \  
HBASE_CLIENT_THREADPOOL_QUEUESIZE=10000 \  
HBASE_CLIENT_THREADPOOL_PRESTART="false" \  
HBASE_CLIENT_ASYNC_ENABLE="false" \  
HBASE_CLIENT_ASYNC_IN_QUEUESIZE=1000 \  
HBASE_CLIENT_ASYNC_FLUSH_PERIOD_MS=100 \  
HBASE_CLIENT_ASYNC_MAX_RETRIES_IN_QUEUE=10 \  
COLLECTOR_TCPLISTENIP=0.0.0.0 \  
COLLECTOR_TCPLISTENPORT=9994 \  
COLLECTOR_TCPWORKERTHREAD=8 \  
COLLECTOR_TCPWORKERQUEUESIZE=1024 \  
COLLECTOR_WORKER_MONITOR="true" \  
COLLECTOR_UDPSTATLISTENIP=0.0.0.0 \  
COLLECTOR_UDPSTATLISTENPORT=9995 \  
COLLECTOR_L4_IP="" \  
COLLECTOR_UDPSTATWORKERTHREAD=8 \  
COLLECTOR_UDPSTATWORKERQUEUESIZE=64 \  
COLLECTOR_UDPSTATWORKER_MONITOR="true" \  
COLLECTOR_UDPSTATSOCKETRECEIVEBUFFERSIZE=4194304 \  
COLLECTOR_UDPSPANLISTENIP=0.0.0.0 \  
COLLECTOR_UDPSPANLISTENPORT=9996 \  
COLLECTOR_UDPSPANWORKERTHREAD=32 \  
COLLECTOR_UDPSPANWORKERQUEUESIZE=256 \  
COLLECTOR_UDPSPANWORKER_MONITOR="true" \  
COLLECTOR_UDPSPANSOCKETRECEIVEBUFFERSIZE=4194304 \  
COLLECTOR_AGENTEVENTWORKER_THREADSIZE=4 \  
COLLECTOR_AGENTEVENTWORKER_QUEUESIZE=1024 \  
STATISTICS_FLUSHPERIOD=1000 \  
CLUSTER_ENABLE="true" \  
CLUSTER_ZOOKEEPER_ADDRESS=localhost \  
CLUSTER_ZOOKEEPER_SESSIONTIMEOUT=30000 \  
CLUSTER_LISTEN_IP="" \  
CLUSTER_LISTEN_PORT="" \  
COLLECTOR_SPANEVENT_SEQUENCE_LIMIT=10000 \  
COLLECTOR_SPAN_FORMAT_COMPATIBILITY_VERSION=v2 \  
COLLECTOR_STAT_FORMAT_COMPATIBILITY_VERSION=v2  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
ADD ./resources /resources  
  
RUN /resources/build && rm -rf resources  
  
ENTRYPOINT ["entrypoint.sh"]  
  
USER tomcat  
  
LABEL "maintainer"="cloudsquad@fxinnovation.com" \  
"org.label-schema.name"="pinpoint-collector" \  
"org.label-schema.base-image.name"="docker.io/library/tomcat" \  
"org.label-schema.base-image.version"="8.5.15-jre8-alpine" \  
"org.label-schema.description"="pinpoint-collector in a container" \  
"org.label-schema.url"="https://github.com/naver/pinpoint" \  
"org.label-schema.vcs-url"="https://bitbucket.org/fxadmin/public-common-
docker-pinpoint_collector" \  
"org.label-schema.vendor"="FXinnovation" \  
"org.label-schema.schema-version"="1.0.0-rc.1" \  
"org.label-schema.applications.java.version"=$JAVA_VERSION \  
"org.label-schema.applications.tomcat.version"=$TOMCAT_VERSION \  
"org.label-schema.applications.confd.version"=$CONFD_VERSION \  
"org.label-schema.applications.pinpoint-
collector.version"=$PINPOINTCOLLECTOR_VERSION \  
"org.label-schema.vcs-ref"=$VCS_REF \  
"org.label-schema.version"=$VERSION \  
"org.label-schema.build-date"=$BUILD_DATE \  
"org.label-schema.usage"="https://bitbucket.org/fxadmin/public-common-docker-
pinpoint_collector"  

