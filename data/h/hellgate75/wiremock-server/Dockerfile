# --- WIREMOCK ---  
FROM ubuntu:16.04  
MAINTAINER Fabrizio Torelli <hellgate75@gmail.com>  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
WIREMOCK_HOME=/wiremock \  
WM_VERSION=2.7.1 \  
WM_DT_VERSION=1.1.6 \  
WM_HTTP_CC_VERSION=5.0-alpha2 \  
DEBIAN_FRONTEND=noninteractive \  
WM_CONFIGURATION_SCRIPT_URL= \  
WM_CERTIFICATE_TAR_GZ_URL= \  
WM_MAPPINGS_TAR_GZ_URL= \  
WM_STATIC_FILES_TAR_GZ_URL= \  
WM_HTTP_PORT=8080 \  
WM_HTTPS_PORT=443 \  
WM_USE_SSL=no \  
VM_VERBOSE=yes \  
WM_BINDING_ADDRESS="0.0.0.0" \  
VM_EXTENSIONS= \  
WM_HTTPS_KEYSTORE= \  
WM_HTTPS_KS_PASSWORD= \  
WM_HTTPS_TRUSTSTORE= \  
WM_HTTPS_TS_PASSWORD= \  
WM_FORCE_REQUIRE_CLIENT_CERT=no \  
WM_RECORD_MAPPING=no \  
VM_MATCH_HEADERS=no \  
VM_PROXY_ALL= \  
VM_PRESERVE_POST_HEADER=no \  
VM_PROXY_VIA= \  
WM_ENABLE_BROWSER_PROXY=no \  
WM_DISABLE_REQUEST_JOURNAL=no \  
WM_CONTAINER_THREADS=10 \  
WM_MAX_REQUESTS_JOURNAL_ENTRIES= \  
WM_JETTY_REQUEST_THREADS= \  
WM_JETTY_QUEUE_SIZE= \  
WM_JETTY_HEADER_BUFFER_SIZE_KB=8192 \  
WM_PRINT_ALL_NETWORK_TRAFFIC=no \  
WM_GLOBAL_RESPONSE_TEMPLATING=no \  
WM_LOCAL_RESPONSE_TEMPLATING=no \  
WIREMOCK_ZOOKEEPER_INTEGRATION_SCRIPT_URL= \  
ZOOKEEPER_CLIENT_SERVICE=no \  
ZOOKEEPER_SERVER_SERVICE=no \  
ZOOKEEPER_SERVER_ADDRESS="localhost:2181" \  
WIREMOCK_SERVICE_PATH= \  
WIREMOCK_ARTIFACT_URL_ENTRY= \  
WIREMOCK_STATIC_URL_ENTRY= \  
WIREMOCK_ZOOKEEPER_SSL_CERTS_URL_ENTRY= \  
ZOOKEEPER_RELEASE=3.5.3-beta \  
ZOOKEEPER_HOME=/usr/lib/zookeeper \  
ZOOKEEPER_PREFIX=/usr/lib/zookeeper \  
ZOO_LOG_DIR=/usr/lib/zookeeper/logs \  
ZOOKEEPER_DATA_FOLDER=/var/local/zookeeper \  
ZOOKEEPER_LOGS_FOLDER=/var/local/zookeeper-logs \  
ZOOKEEPER_SSL_FOLDER=/usr/local/zookeeper-ssl \  
ZK_ADMIN_SERVER_ADDRESS=8181 \  
ZOOKEEPER_SERVER_CONFIG_URL_ENTRY= \  
ZOOKEEPER_SERVER_CONFIG_SCRIPT_URL_ENTRY= \  
ZOOKEEPER_SEEK_INTERVAL_MIN=15 \  
ZOOKEEPER_SEEK_INTERVAL_HOUR= \  
ZOOKEEPER_SERVER_HOST=localhost \  
ZOOKEEPER_SERVER_PORT=2181 \  
LOG_ON_ZOOKEEPER=no \  
ZOOKEEPER_LOG_INTERVAL_MIN=15 \  
ZOOKEEPER_LOG_INTERVAL_HOUR= \  
CURRENT_SERVER_PATH= \  
CURRENT_SERVER_ID= \  
PATH=$PATH:/usr/lib/zookeeper/bin  
  
  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install apt-utils \  
&& apt-get -y install software-properties-common \  
&& apt-get -y install wget curl htop git vim net-tools inetutils-tools
inetutils-ping \  
&& add-apt-repository -y -u ppa:webupd8team/java \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& echo -e "\n" | apt-get -y install oracle-java8-installer oracle-java8-set-
default \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /wiremock \  
&& mkdir /wiremock/mappings \  
&& mkdir /wiremock/__files \  
&& mkdir /wiremock/certificates  
  
WORKDIR /wiremock  
  
RUN curl -sSL -o wiremock-standalone.jar
http://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/$WM_VERSION/wiremock-standalone-$WM_VERSION.jar  
RUN curl -sSL -o body-transformer.jar
http://central.maven.org/maven2/com/opentable/wiremock-body-
transformer/$WM_DT_VERSION/wiremock-body-transformer-$WM_DT_VERSION.jar  
RUN curl -sSL -o httpcomponents-client.tar.gz
https://archive.apache.org/dist/httpcomponents/httpclient/binary/httpcomponents-
client-$WM_HTTP_CC_VERSION-bin.tar.gz  
RUN tar -xzf httpcomponents-client.tar.gz  
  
RUN curl -sSL http://www-
eu.apache.org/dist/zookeeper/zookeeper-$ZOOKEEPER_RELEASE/zookeeper-$ZOOKEEPER_RELEASE.tar.gz
| tar -x -C /usr/lib/ \  
&& cd /usr/lib && ln -s zookeeper-* zookeeper \  
&& mkdir -p $ZOOKEEPER_DATA_FOLDER \  
&& mkdir -p ZOOKEEPER_LOGS_FOLDER \  
&& mkdir -p $ZOOKEEPER_SSL_FOLDER \  
&& mkdir -p $ZOOKEEPER_HOME/conf \  
&& mkdir -p $ZOOKEEPER_HOME/logs \  
&& mkdir -p /root/.wiremock \  
&& mkdir -p /root/.zookeeper \  
&& echo "head-zookeeper" >> /root/.bashrc \  
&& echo "head-wiremock" >> /root/.bashrc \  
&& echo ". setenv-zookeeper" >> /root/.bashrc \  
&& echo ". custom-setenv-zookeeper" >> /root/.bashrc  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY docker-start-wiremock.sh /docker-start-wiremock.sh  
COPY start-wiremock-server.sh /usr/local/bin/start-wiremock-server  
COPY stop-wiremock-server.sh /usr/local/bin/stop-wiremock-server  
COPY status-wiremock-server.sh /usr/local/bin/status-wiremock-server  
COPY head-wiremock.sh /usr/local/bin/head-wiremock  
COPY set-job-wiremock.sh /usr/local/bin/set-crontab-job  
COPY dump-env.sh /usr/local/bin/dump-env  
COPY init.wiremock.sh /etc/init.d/wiremock  
COPY default.wiremock.sh /etc/default/wiremock  
  
ADD zookeeper/zookeeper.cfg.standalone.template
$ZOOKEEPER_HOME/conf/zoo.cfg.standalone.template  
ADD zookeeper/zookeeper.cfg.replica.template
$ZOOKEEPER_HOME/conf/zoo.cfg.replica.template  
COPY zookeeper/start-zookeeper.sh /usr/local/bin/start-zookeeper  
COPY zookeeper/status-zookeeper.sh /usr/local/bin/status-zookeeper  
COPY zookeeper/stop-zookeeper.sh /usr/local/bin/stop-zookeeper  
COPY zookeeper/head-zookeeper.sh /usr/local/bin/head-zookeeper  
COPY zookeeper/configure-zookeeper.sh /usr/local/bin/configure-zookeeper  
COPY zookeeper/init_default_env_zookeeper.sh /usr/local/bin/setenv-zookeeper  
COPY zookeeper/init_custom_env_zookeeper.sh /usr/local/bin/custom-setenv-
zookeeper  
COPY zookeeper/init_custom_env_zookeeper.sh /root/.wiremock/bkp-custom-setenv-
zookeeper  
COPY zookeeper/client-seek-zookeeper.sh /usr/local/bin/seek-zookeeper  
COPY zookeeper/client-log-zookeeper.sh /usr/local/bin/log-zookeeper  
COPY zookeeper/load-zookeeper-data.sh /usr/local/bin/import-data-zookeeper  
COPY zookeeper/get-zookeeper-node.sh /usr/local/bin/get-node-zookeeper  
COPY zookeeper/set-zookeeper-node.sh /usr/local/bin/set-node-zookeeper  
COPY zookeeper/log4j.properties /usr/lib/zookeeper/conf/log4j.properties  
COPY zookeeper/default-setenv-zookeeper.sh /root/.zookeeper/default-setenv-
zookeeper.sh  
COPY zookeeper/crontab /etc/crontab  
  
RUN chmod 777 /docker-start-wiremock.sh \  
&& chmod 777 /docker-entrypoint.sh \  
&& chmod 777 /usr/local/bin/*-wiremock* \  
&& chmod 777 /usr/local/bin/*zookeeper \  
&& chmod 777 /usr/local/bin/set-crontab-job \  
&& chmod 644 /etc/crontab \  
&& chmod 777 /usr/local/bin/dump-env \  
&& chmod 777 /etc/init.d/wiremock \  
&& chmod 777 /etc/default/wiremock  
  
VOLUME ["/wiremock/mappings", "/wiremock/__files", "/wiremock/certificates",
"/var/local/zookeeper", "/var/local/zookeeper-logs", "/var/local/zookeeper-
ssl"]  
  
CMD /docker-start-wiremock.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8080 443 8081 2181 2182  

