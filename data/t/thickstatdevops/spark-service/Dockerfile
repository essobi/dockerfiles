FROM openjdk:jre-alpine  
  
MAINTAINER Saravanan Elumalai <saravanane@thickstat.com>  
  
# Scala related variables.  
ARG SCALA_VERSION=2.12.2  
ARG SCALA_BINARY_ARCHIVE_NAME=scala-${SCALA_VERSION}  
ARG
SCALA_BINARY_DOWNLOAD_URL=http://downloads.lightbend.com/scala/${SCALA_VERSION}/${SCALA_BINARY_ARCHIVE_NAME}.tgz  
  
# Spark related variables.  
ARG SPARK_VERSION=2.2.0  
ARG SPARK_BINARY_ARCHIVE_NAME=spark-${SPARK_VERSION}-bin-hadoop2.7  
#ARG
SPARK_BINARY_DOWNLOAD_URL=http://apache.cs.utah.edu/spark/spark-${SPARK_VERSION}/${SPARK_BINARY_ARCHIVE_NAME}.tgz  
ARG
SPARK_BINARY_DOWNLOAD_URL=http://d3kbcqa49mib13.cloudfront.net/${SPARK_BINARY_ARCHIVE_NAME}.tgz  
  
# Configure env variables for Scala, SBT and Spark.  
# Also configure PATH env variable to include binary folders of Java, Scala,
SBT and Spark.  
ENV SCALA_HOME /usr/local/scala  
ENV SPARK_HOME /usr/local/spark  
ENV PATH $JAVA_HOME/bin:$SCALA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH  
# Download, uncompress and move all the required packages and libraries to
their corresponding directories in /usr/local/ folder.  
RUN apk --update add vim screen tmux procps coreutils  
RUN apk add \--no-cache bash  
RUN apk --update add \--virtual build-dependencies wget && \  
wget -qO - ${SCALA_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \  
wget -qO - ${SPARK_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \  
cd /usr/local/ && \  
ln -s ${SCALA_BINARY_ARCHIVE_NAME} scala && \  
ln -s ${SPARK_BINARY_ARCHIVE_NAME} spark && \  
cp spark/conf/log4j.properties.template spark/conf/log4j.properties && \  
sed -i -e s/WARN/ERROR/g spark/conf/log4j.properties && \  
sed -i -e s/INFO/ERROR/g spark/conf/log4j.properties && \  
sed -i -e s/8080/8082/g spark/sbin/start-master.sh && \  
apk del build-dependencies  
  
# We will be running our Spark jobs as `root` user.  
USER root  
  
# Working directory is set to the home folder of `root` user.  
WORKDIR /root  
  
# Expose ports for monitoring.  
# SparkContext web UI on 4040 -- only available for the duration of the
application.  
# Spark master’s web UI on 8082.  
# Spark worker web UI on 8081.  
EXPOSE 4040 8081 8082  
  
CMD ["/bin/bash"]

