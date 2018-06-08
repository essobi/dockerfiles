FROM ubuntu:16.10  
# install Java 8 & curl  
RUN apt-get -y update && \  
apt-get -y install dirmngr wget curl && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu yakkety main" >
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu yakkety main"
>> /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get -y update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java8-installer
oracle-java8-set-default  
  
# download and install spark  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
| tar -xz -C /usr/local/ && \  
mv /usr/local/spark-2.1.0-bin-hadoop2.7 /usr/local/spark  
  
# copy some scripts to run spark  
COPY scripts/start-master.sh /start-master.sh  
COPY scripts/start-worker.sh /start-worker.sh  
COPY scripts/spark-shell.sh /spark-shell.sh  
COPY scripts/spark-defaults.conf /spark-defaults.conf  
  
# copy the connector to cassandra  
#COPY jars/spark-cassandra-connector-assembly-1.6.0-M1-s_2.10.jar /spark-
cassandra-connector-assembly-1.6.0-M1-s_2.10.jar  
# configure spark  
ENV SPARK_HOME /usr/local/spark  
ENV SPARK_MASTER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_WORKER_OPTS="$SPARK_MASTER_OPTS -Dspark.worker.cleanup.enabled=true
-Dspark.shuffle.service.enabled=true"  
ENV SPARK_MASTER_PORT 7077  
ENV SPARK_MASTER_WEBUI_PORT 8080  
ENV SPARK_WORKER_PORT 8888  
ENV SPARK_WORKER_WEBUI_PORT 8081  
### Spark ports  
# 4040: spark ui  
# 7001: spark driver  
# 7002: spark fileserver  
# 7003: spark broadcast  
# 7004: spark replClassServer  
# 7005: spark blockManager  
# 7006: spark executor  
# 7077: spark master  
# 8080: spark master ui  
# 8081: spark worker ui  
# 8888: spark worker  
EXPOSE 4040 7001 7002 7003 7004 7005 7006 7077 8080 8081 8888  
# by default, this container is a Spark Worker  
CMD ["/start-worker.sh"]  

