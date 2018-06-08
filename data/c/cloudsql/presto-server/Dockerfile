FROM java:8  
MAINTAINER Chuan Liu <liuchuan@liuchuan.org>  
  
# Dockerize  
ENV DOCKERIZE_VERSION v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Presto  
ENV PRESTO_VERSION=0.150 \  
PRESTO_DISCOVERY_URI= \  
PRESTO_DISCOVERY_SERVER_ENABLED=true \  
PRESTO_HOME=/usr/local/presto \  
PRESTO_CONFIG_HOME=/usr/local/presto/etc \  
PRESTO_HTTP_SERVER_PORT=8080 \  
PRESTO_IS_COORDINATOR=true \  
PRESTO_JVM_MEMORY= \  
PRESTO_LOG_LEVEL=INFO \  
PRESTO_MULTIPLE_TASKS_PER_NODE_ENABLED=true \  
PRESTO_NODE_ENVIRONMENT=default \  
PRESTO_NODE_SCHEDULER_INCLUDE_COORDINATOR=true \  
PRESTO_OPTIMIZER_USE_INTERMEDIATE_AGGREGATIONS=true \  
PRESTO_QUERY_MAX_MEMORY=1024GB \  
PRESTO_QUERY_MAX_MEMORY_PER_NODE=  
  
  
RUN mkdir -p $PRESTO_HOME  
WORKDIR $PRESTO_HOME  
  
ENV PRESTO_TGZ_URL https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/$PRESTO_VERSION/presto-server-$PRESTO_VERSION.tar.gz  
ENV PRESTO_TGZ_SHA1_URL $PRESTO_TGZ_URL.sha1  
  
RUN set -x \  
&& apt-get update && apt-get install -y uuid-runtime \  
&& PRESTO_TGZ_SHA1=$(curl -fsSL $PRESTO_TGZ_SHA1_URL) \  
&& curl -fsSL "$PRESTO_TGZ_URL" -o presto.tar.gz \  
&& echo "$PRESTO_TGZ_SHA1 presto.tar.gz" | sha1sum -c - \  
&& tar -xvf presto.tar.gz --strip-components=1 \  
&& rm presto.tar.gz* \  
&& apt-get clean  
  
COPY templates $PRESTO_CONFIG_HOME  
COPY presto_entrypoint.sh $PRESTO_HOME/entrypoint  
  
# Add hadoop-azure to allow querying data in Azure storage  
# as a workaround for the following PR (before it can be merged):  
# https://github.com/prestodb/presto-hadoop-apache2/pull/14  
ENV HADOOP_AZURE_URL http://repo1.maven.org/maven2/org/apache/hadoop/hadoop-
azure/2.7.2/hadoop-azure-2.7.2.jar  
ENV AZURE_STORAGE_URL http://repo1.maven.org/maven2/com/microsoft/azure/azure-
storage/2.2.0/azure-storage-2.2.0.jar  
ENV COMMONS_LANG_URL http://repo1.maven.org/maven2/commons-lang/commons-
lang/2.6/commons-lang-2.6.jar  
ENV JETTY_UTIL_URL http://repo1.maven.org/maven2/org/mortbay/jetty/jetty-
util/6.1.26/jetty-util-6.1.26.jar  
  
ENV HIVE_HADOOP2_HOME $PRESTO_HOME/plugin/hive-hadoop2  
  
RUN set -x \  
&& wget -P "${HIVE_HADOOP2_HOME}" "${HADOOP_AZURE_URL}" \  
&& wget -P "${HIVE_HADOOP2_HOME}" "${AZURE_STORAGE_URL}" \  
&& wget -P "${HIVE_HADOOP2_HOME}" "${COMMONS_LANG_URL}" \  
&& wget -P "${HIVE_HADOOP2_HOME}" "${JETTY_UTIL_URL}"  
  
ENTRYPOINT ["/usr/local/presto/entrypoint"]  

