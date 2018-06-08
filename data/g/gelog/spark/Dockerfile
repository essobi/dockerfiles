  
# Inspired by these images:  
# https://github.com/sequenceiq/docker-spark  
# https://github.com/apache/spark/tree/master/docker  
# For building this image, See https://github.com/GELOG/docker-ubuntu-java  
FROM gelog/java:openjdk7  
  
MAINTAINER Francois Langelier  
  
ENV WGET_VERSION 1.15-1ubuntu1.14.04.1  
ENV SPARK_VERSION 1.2.1  
ENV SPARK_BIN_VERSION $SPARK_VERSION-bin-hadoop2.3  
ENV SPARK_HOME /usr/local/spark  
ENV PATH $PATH:$SPARK_HOME/bin  
  
# Installing wget  
RUN \  
apt-get update && \  
apt-get install -y wget=$WGET_VERSION && \  
rm -rf /var/lib/apt/lists/*  
  
# Installing Spark for Hadoop  
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_BIN_VERSION.tgz &&
\  
tar -zxf /spark-$SPARK_BIN_VERSION.tgz -C /usr/local/ && \  
ln -s /usr/local/spark-$SPARK_BIN_VERSION $SPARK_HOME && \  
rm /spark-$SPARK_BIN_VERSION.tgz  
  
# Default action: show available commands on startup  
CMD ["spark-submit"]  
  

