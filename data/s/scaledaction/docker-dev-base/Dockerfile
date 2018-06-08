FROM java:7  
MAINTAINER Scaled Action  
  
ENV SPARK_VERSION 1.4.1  
ENV SCALA_VERSION 2.10  
ENV HADOOP_VERSION 2.6  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_VERSION-bin-
hadoop$HADOOP_VERSION.tgz | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION
spark  
ENV SPARK_HOME /usr/local/spark  
  
RUN wget -q http://central.maven.org/maven2/org/apache/spark/spark-streaming-
kafka_$SCALA_VERSION/$SPARK_VERSION/spark-streaming-
kafka_$SCALA_VERSION-$SPARK_VERSION.jar  
  

