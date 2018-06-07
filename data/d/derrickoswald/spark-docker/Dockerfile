FROM singularities/hadoop:2.7  
MAINTAINER Singularities  
  
# Version  
ENV SPARK_VERSION=2.3.0  
# set up TTY  
ENV TERM=xterm-256color  
  
# Set home  
ENV SPARK_HOME=/usr/local/spark-$SPARK_VERSION  
  
# Install dependencies  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install \  
-yq --no-install-recommends \  
python python3 vim sqlite3 r-base p7zip net-tools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install GridLAB-D  
COPY gridlabd_3.2.0-2_amd64.deb /opt/util/gridlabd_3.2.0-2_amd64.deb  
RUN dpkg -i /opt/util/gridlabd_3.2.0-2_amd64.deb \  
&& rm /opt/util/gridlabd_3.2.0-2_amd64.deb  
  
# Install Spark  
RUN mkdir -p "${SPARK_HOME}" \  
&& export ARCHIVE=spark-$SPARK_VERSION-bin-hadoop2.7.tgz \  
&& export DOWNLOAD_PATH=mirror/apache/dist/spark/spark-$SPARK_VERSION/$ARCHIVE
\  
&& curl -sSL http://mirror.switch.ch/$DOWNLOAD_PATH | \  
tar -xz -C $SPARK_HOME \--strip-components 1 \  
&& sed 's/log4j.rootCategory=INFO/log4j.rootCategory=WARN/g'
$SPARK_HOME/conf/log4j.properties.template >$SPARK_HOME/conf/log4j.properties
\  
&& echo '' >> $SPARK_HOME/conf/log4j.properties \  
&& echo '# quiet the apache logs' >> $SPARK_HOME/conf/log4j.properties \  
&& echo 'log4j.logger.org.apache=ERROR' >> $SPARK_HOME/conf/log4j.properties \  
&& rm -rf $ARCHIVE  
COPY spark-env.sh $SPARK_HOME/conf/spark-env.sh  
ENV PATH=$PATH:$SPARK_HOME/bin  
  
# Install Cassandra  
RUN echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | tee -a
/etc/apt/sources.list.d/cassandra.sources.list  
RUN curl https://www.apache.org/dist/cassandra/KEYS | apt-key add -  
RUN apt-get update \  
&& apt-key adv --keyserver pool.sks-keyservers.net --recv-key A278B781FE4B2BDA  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
cassandra  
RUN apt-get clean  
  
# Remove duplicate SLF4J bindings  
RUN mv /usr/local/spark-$SPARK_VERSION/jars/slf4j-log4j12-1.7.16.jar
/usr/local/spark-$SPARK_VERSION/jars/slf4j-log4j12-1.7.16.jar.hide  
  
# fix missing ps command  
RUN apt-get update \  
&& apt-get install -yq --reinstall procps  
  
# Spark ports, see
https://spark.apache.org/docs/latest/security.html#configuring-ports-for-
network-security  
# Cluster Manager Web UI  
EXPOSE 4040  
# Standalone Master REST port (spark.master.rest.port)  
EXPOSE 6066  
# Driver to Standalone Master  
EXPOSE 7077  
# Standalone Master Web UI  
EXPOSE 8080  
# Standalone Worker Web UI  
EXPOSE 8081  
# Yarn Resource Manager  
EXPOSE 8088  
# Rstudio  
EXPOSE 8787  
# History Server  
EXPOSE 18080  
# Hadoop ports, see https://hadoop.apache.org/docs/r2.7.4/hadoop-project-
dist/hadoop-hdfs/hdfs-default.xml  
# DFS Namenode IPC  
EXPOSE 8020  
# DFS Datanode data transfer  
EXPOSE 50010  
# DFS Datanode IPC  
EXPOSE 50020  
# DFS Namenode Web UI  
EXPOSE 50070  
# DFS Datanode Web UI  
EXPOSE 50075  
# DFS Secondary Namenode Web UI  
EXPOSE 50090  
# DFS Backup Node data transfer  
EXPOSE 50100  
# DFS Backup Node Web UI  
EXPOSE 50105  
# Cassandra ports  
# Cassandra storage_port  
EXPOSE 7000  
# Cassandra ssl_storage_port  
EXPOSE 7001  
# Cassandra JMX monitoring port  
# EXPOSE 7199  
# Cassandra native_transport_port  
EXPOSE 9042  
# Cassandra rpc_port  
EXPOSE 9160  
# Copy start script  
COPY start-spark /opt/util/bin/start-spark  
  
# Fix Java native library path  
# avoid WARN NativeCodeLoader: Unable to load native-hadoop library for your
platform... using builtin-java classes where applicable  
COPY spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf  
RUN ldconfig  
  
# Fix environment for other users  
RUN echo "export SPARK_HOME=$SPARK_HOME" >> /etc/bash.bashrc \  
&& echo 'export PATH=$PATH:$SPARK_HOME/bin'>> /etc/bash.bashrc \  
&& echo "alias ll='ls -alF'">> /etc/bash.bashrc  
  

