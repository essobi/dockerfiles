FROM tomcat:8.5.16-jre8-alpine  
  
ENV PINPOINTWEB_VERSION=1.6.2 \  
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
HBASE_CLIENT_PARALLEL_SCAN_ENABLE="true" \  
HBASE_CLIENT_PARALLEL_SCAN_MAXTHREADS=64 \  
HBASE_CLIENT_PARALLEL_SCAN_MAXTHREADSPERSCAN=16 \  
CLUSTER_ENABLE="true" \  
CLUSTER_WEB_TCP_PORT=9997 \  
CLUSTER_ZOOKEEPER_ADDRESS=localhost \  
CLUSTER_ZOOKEEPER_SESSIONTIMEOUT=30000 \  
CLUSTER_ZOOKEEPER_RETRY_INTERVAL=60000 \  
CLUSTER_CONNECT_ADDRESS="" \  
ADMIN_PASSWORD=changeme \  
CONFIG_SENDUSAGE="true" \  
CONFIG_EDITUSERINFO="true" \  
CONFIG_OPENSOURCE="true" \  
CONFIG_SHOW_ACTIVETHREAD="true" \  
CONFIG_SHOW_ACTIVETHREADDUMP="true" \  
CONFIG_SHOW_INSPECTOR_DATASOURCE="true" \  
CONFIG_ENABLE_ACTIVETHREADDUMP="true" \  
WEB_SELECTSPANS_LIMIT=500 \  
WEB_SELECTALLSPANS_LIMIT=500 \  
WEB_ACTIVETHREAD_ACTIVEAGENT_DURATION_DAYS=7 \  
WEB_SPAN_FORMAT_COMPATIBILITY_VERSION=compatibilityMode \  
WEB_STAT_FORMAT_COMPATIBILITY_VERSION=compatibilityMode  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
ADD ./resources /resources  
  
RUN /resources/build && rm -rf resources  
  
ENTRYPOINT ["entrypoint.sh"]  
  
USER tomcat  
  
LABEL "maintainer"="cloudsquad@fxinnovation.com" \  
"org.label-schema.name"="pinpoint-web" \  
"org.label-schema.base-image.name"="docker.io/library/tomcat" \  
"org.label-schema.base-image.version"="8.5.16-jre8-alpine" \  
"org.label-schema.description"="pinpoint-web in a container" \  
"org.label-schema.url"="https://github.com/naver/pinpoint" \  
"org.label-schema.vcs-url"="https://bitbucket.org/fxadmin/public-common-
docker-pinpoint_web" \  
"org.label-schema.vendor"="FXinnovation" \  
"org.label-schema.schema-version"="1.0.0-rc.1" \  
"org.label-schema.applications.java.version"=$JAVA_VERSION \  
"org.label-schema.applications.tomcat.version"=$TOMCAT_VERSION \  
"org.label-schema.applications.confd.version"=$CONFD_VERSION \  
"org.label-schema.applications.pinpoint-web.version"=$PINPOINTWEB_VERSION \  
"org.label-schema.vcs-ref"=$VCS_REF \  
"org.label-schema.version"=$VERSION \  
"org.label-schema.build-date"=$BUILD_DATE \  
"org.label-schema.usage"="https://bitbucket.org/fxadmin/public-common-docker-
pinpoint_web"  

