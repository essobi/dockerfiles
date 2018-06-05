FROM dataiku/dss:4.1.5  
  
MAINTAINER Cedric DUE <cedric@saagie.com>  
  
USER root  
  
RUN apt-get update && apt-get install -y wget gnupg2 lsb-release  
  
RUN wget
http://apache.mirrors.tds.net/hadoop/common/hadoop-2.6.5/hadoop-2.6.5.tar.gz
&& \  
mkdir -p /etc/hadoop && \  
tar -xzf hadoop-2.6.5.tar.gz -C /etc/hadoop --strip-components=1  
  
RUN wget https://archive.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-
hadoop2.6.tgz && \  
mkdir -p /opt/spark && \  
tar -xzf spark-2.1.0-bin-hadoop2.6.tgz -C /opt/spark --strip-components=1  
# Grant acces to /opt/spark to anybody so that dataiku user can override
spark-env.sh  
RUN chmod -R 777 /opt/spark  
  
COPY run-dataiku.sh /home/dataiku  
RUN chown dataiku:dataiku /home/dataiku/run-dataiku.sh && \  
chmod 755 /home/dataiku/run-dataiku.sh  
  
# Install Mesos 1.3.1  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]') && \  
CODENAME=$(lsb_release -cs) && \  
echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | tee
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get -y update && \  
apt-get install -y --no-install-recommends systemd mesos=1.3.1-2.0.1  
# Install DSS dependencies  
RUN echo "APT::Get::Assume-Yes "true";\nAPT::Get::force-yes "true";" >
/etc/apt/apt.conf.d/90forceyes  
RUN /home/dataiku/dataiku-dss-4.1.5/scripts/install/install-deps.sh -without-
java -without-python -with-r  
  
# Python Env requirements  
RUN apt-get install -y build-essential python-dev  
  
USER dataiku  
  
RUN mkdir /home/dataiku/lib/  
RUN wget http://central.maven.org/maven2/org/apache/hive/hive-
common/1.1.0/hive-common-1.1.0.jar -P /home/dataiku/lib/ && \  
wget http://central.maven.org/maven2/org/apache/hive/hive-service/1.1.0/hive-
service-1.1.0.jar -P /home/dataiku/lib/ && \  
wget http://central.maven.org/maven2/org/apache/hive/hive-jdbc/1.1.0/hive-
jdbc-1.1.0.jar -P /home/dataiku/lib/ && \  
wget http://central.maven.org/maven2/org/apache/spark/spark-
hive_2.11/2.1.0/spark-hive_2.11-2.1.0.jar -P /home/dataiku/lib/ && \  
wget
http://central.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.3/httpclient-4.5.3.jar
-P /home/dataiku/lib/ && \  
wget
http://central.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.7/httpcore-4.4.7.jar
-P /home/dataiku/lib/ && \  
wget
http://central.maven.org/maven2/org/apache/thrift/libthrift/0.9.2/libthrift-0.9.2.jar
-P /home/dataiku/lib/ && \  
wget
https://downloads.cloudera.com/connectors/Cloudera_ImpalaJDBC_2.5.5.1007.zip
-P /home/dataiku/lib/ && \  
wget
https://repository.cloudera.com/content/repositories/releases/com/twitter/parquet-
hadoop-bundle/1.5.0-cdh5.7.1/parquet-hadoop-bundle-1.5.0-cdh5.7.1.jar -P
/home/dataiku/lib/ && \  
cd /home/dataiku/lib/ && \  
unzip -j Cloudera_ImpalaJDBC_2.5.5.1007.zip && unzip -j
Cloudera_ImpalaJDBC4_2.5.5.1007.zip && \  
rm -f *.zip  
  
# Remove libthrift-0.9.0 and TCLIServiceClient.jar (coming with
Cloudera_ImpalaJDBC_2.5.5.1007.zip)  
RUN rm -f /home/dataiku/lib/libthrift-0.9.0.jar
/home/dataiku/lib/TCLIServiceClient.jar  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre/  
ENV PATH $PATH:/etc/hadoop/bin/:/etc/hadoop/sbin:/opt/spark/bin  
ENV HADOOP_CONF_DIR /etc/hadoop/conf  
ENV HIVE_CONF_DIR /etc/hive/conf  
ENV HADOOP_HOME /etc/hadoop  
ENV HADOOP_LIB_EXEC /etc/hadoop/libexec/  
ENV SPARK_HOME /opt/spark  
ENV JAVA_LIBRARY_PATH $HADOOP_HOME/lib/native  
ENV LD_LIBRARY_PATH $HADOOP_HOME/lib/native  
ENV MESOS_NATIVE_JAVA_LIBRARY /usr/lib/libmesos-1.3.1.so  
ENV JAVA_VERSION 8.131  
ENV SPARK_VERSION 2.1.0  
ENV APACHE_SPARK_VERSION 2.1.0  
  
ENTRYPOINT ["/home/dataiku/run-dataiku.sh"]  

