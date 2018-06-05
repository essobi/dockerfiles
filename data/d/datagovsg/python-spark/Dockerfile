FROM python:2.7  
# Setup Java  
RUN set -x && \  
apt-get update && \  
apt-get install --no-install-recommends -y software-properties-common && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > \  
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >>
\  
/etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && echo yes | apt-get install -y --force-yes oracle-
java8-installer && \  
apt-get update && apt-get install oracle-java8-set-default && \  
apt-get remove software-properties-common -y --auto-remove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ARG HADOOP_VERSION=2.6.1  
ARG SPARK_VERSION=1.6.1  
# Setup Hadoop variables  
ENV HADOOP_HOME /opt/hadoop  
ENV PATH ${PATH}:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin  
ENV HADOOP_MAPRED_HOME ${HADOOP_HOME}  
ENV HADOOP_COMMON_HOME ${HADOOP_HOME}  
ENV HADOOP_HDFS_HOME ${HADOOP_HOME}  
ENV YARN_HOME ${HADOOP_HOME}  
ENV HADOOP_COMMON_LIB_NATIVE_DIR ${HADOOP_HOME}/lib/native  
ENV HADOOP_OPTS "-Djava.library.path=${HADOOP_HOME}/lib"  
ENV HDFS_CONF_DIR ${HADOOP_HOME}/etc/hadoop  
ENV YARN_CONF_DIR ${HADOOP_HOME}/etc/hadoop  
ENV HADOOP_CONF_DIR ${HADOOP_HOME}/etc/hadoop  
  
# Setup Hive  
ENV HIVE_CONF_DIR ${HADOOP_CONF_DIR}  
  
# Setup Spark  
ENV SPARK_16_HOME=/opt/spark-${SPARK_16_VERSION}  
ENV SPARK_20_HOME=/opt/spark-${SPARK_20_VERSION}  
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}  
ENV PYSPARK_PYTHON=python  
ENV PATH=$PATH:${SPARK_HOME}/bin  
  
# Add these two spark packages when submitting PySpark applications  
RUN if [ "${SPARK_VERSION}" = "${SPARK_16_HOME}" ]; then \  
export PYSPARK_SUBMIT_ARGS="--packages com.databricks:spark-
csv_2.10:1.5.0,com.databricks:spark-
avro_2.10:2.0.1,graphframes:graphframes:0.1.0-spark1.6 pyspark-shell"; \  
export
PYTHONPATH=${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-0.9-src.zip; \  
elif [ "${SPARK_VERSION}" = "${SPARK_20_HOME}" ]; then \  
export PYSPARK_SUBMIT_ARGS="--packages com.databricks:spark-
csv_2.11:1.5.0,com.databricks:spark-
avro_2.11:3.1.0,graphframes:graphframes:0.3.0-spark2.0-s_2.11 pyspark-shell";
\  
export
PYTHONPATH=${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-0.10.3-src.zip;
\  
fi  
  
# Exposes the relevant ports and setup the port settings  
ENV SPARK_MASTER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_WORKER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_MASTER_PORT 7077  
ENV SPARK_MASTER_WEBUI_PORT 8080  
ENV SPARK_WORKER_PORT 8888  
ENV SPARK_WORKER_WEBUI_PORT 8081  
# Set up Sqoop  
ENV SQOOP_HOME /opt/sqoop  
ENV PATH ${PATH}:${SQOOP_HOME}/bin:${HADOOP_HOME}/bin  
  
# Download binaries  
COPY install.sh /install.sh  
RUN /install.sh  
  
EXPOSE 8080 7077 8888 8081 4040 7001 7002 7003 7004 7005 7006  
RUN echo $PYSPARK_SUBMIT_ARGS  
  
CMD '/bin/bash'  

