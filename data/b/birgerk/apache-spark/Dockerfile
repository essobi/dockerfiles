FROM phusion/baseimage:0.9.22  
MAINTAINER BirgerK <birger.kamp@gmail.com>  
  
ENV SPARK_VERSION 2.2.1  
ENV SPARK_INSTALL /usr/local  
ENV SPARK_HOME $SPARK_INSTALL/spark  
ENV SPARK_ROLE master  
ENV HADOOP_VERSION 2.7  
ENV SPARK_MASTER_PORT 7077  
ENV PYSPARK_PYTHON python3  
ENV DOCKERIZE_VERSION v0.2.0  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk autossh python3-pip git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
##### INSTALL DOCKERIZE  
RUN curl -L -O
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm -rf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
##### INSTALL APACHE SPARK WITH HDFS  
RUN curl -s
http://mirror.synyx.de/apache/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-hadoop$HADOOP_VERSION.tgz | tar -xz -C $SPARK_INSTALL && \  
cd $SPARK_INSTALL && ln -s spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION
spark  
  
##### Build spark-influx-sink and copy to spark-jars  
RUN mkdir -p /tmp/spark-influx-sink && git clone
https://github.com/palantir/spark-influx-sink.git /tmp/spark-influx-sink && \  
cd /tmp/spark-influx-sink && ./gradlew build && cp spark-influx-
sink/build/libs/spark-influx-sink-*.jar /usr/local/spark/jars && \  
cd $SPARK_HOME && rm -rf /tmp/spark-influx-sink ~/.m2 ~/.gradle  
  
RUN curl -o /usr/local/spark/jars/dropwizard-metrics-influxdb-1.2.2.jar
http://central.maven.org/maven2/com/izettle/dropwizard-metrics-
influxdb/1.2.2/dropwizard-metrics-influxdb-1.2.2.jar  
  
WORKDIR $SPARK_HOME  
  
##### ADD Scriptss  
RUN mkdir /etc/service/spark  
ADD runit/spark.sh /etc/service/spark/run  
RUN chmod +x /etc/service/**/*  
  
EXPOSE 4040 6066 7077 7078 8080 8081 8888  
VOLUME ["$SPARK_HOME/logs"]  
  
CMD ["/sbin/my_init"]  

