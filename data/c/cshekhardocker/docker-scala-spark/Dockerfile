FROM openjdk:8  
MAINTAINER c-shekhar  
  
# Scala related variables.  
ARG SCALA_VERSION=2.10.4  
ARG SCALA_BINARY_ARCHIVE_NAME=scala-${SCALA_VERSION}  
ARG
SCALA_BINARY_DOWNLOAD_URL=http://downloads.lightbend.com/scala/${SCALA_VERSION}/${SCALA_BINARY_ARCHIVE_NAME}.tgz  
  
# SBT related variables.  
ARG SBT_VERSION=0.13.8  
ARG SBT_BINARY_ARCHIVE_NAME=sbt-$SBT_VERSION  
ARG SBT_BINARY_DOWNLOAD_URL=https://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/${SBT_BINARY_ARCHIVE_NAME}.tgz  
  
# Spark related variables.  
ARG SPARK_VERSION=1.5.2  
ARG SPARK_BINARY_ARCHIVE_NAME=spark-${SPARK_VERSION}-bin-hadoop2.6  
ARG
SPARK_BINARY_DOWNLOAD_URL=http://d3kbcqa49mib13.cloudfront.net/${SPARK_BINARY_ARCHIVE_NAME}.tgz  
  
# Configure env variables for Scala, SBT and Spark.  
# Also configure PATH env variable to include binary folders of Java, Scala,
SBT and Spark.  
ENV SCALA_HOME /usr/local/scala  
ENV SBT_HOME /usr/local/sbt  
ENV SPARK_HOME /usr/local/spark  
ENV MONGO_HOME /usr/local/mongodb-linux-x86_64-ubuntu1404-3.0.4  
ENV PATH
$MONGO_HOME/bin:$JAVA_HOME/bin:$SCALA_HOME/bin:$SBT_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH  
  
# Download, uncompress and move all the required packages and libraries to
their corresponding directories in /usr/local/ folder.  
RUN apt-get -yqq update && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
# wget
"http://archive.ubuntu.com/ubuntu/pool/universe/m/mongodb/mongodb_2.6.10-0ubuntu1_i386.deb"
&& \  
# apt-get -y update && \  
# apt-get -y install mongodb && \  
# export PATH=mongodb-linux-x86_64-amazon-3.0.4/bin:$PATH && \  
wget "downloads.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1404-3.0.4.tgz"
&& tar -zxvf mongodb-linux-x86_64-ubuntu1404-3.0.4.tgz -C /usr/local/ && \  
mkdir -p /data/db && \  
apt-get -y update && \  
apt-get -y install libssl1.0.0 libssl-dev && \  
cd /lib/x86_64-linux-gnu && \  
ln -s libssl.so.1.0.0 libssl.so.10 && \  
ln -s libcrypto.so.1.0.0 libcrypto.so.10 && \  
# ln -s /lib/x86_64-linux-gnu/libssl.so.1.0.0 /usr/lib/libssl.so.10 && \  
# ln -s /lib/x86_64-linux-gnu/libcrypto.so.1.0.0 /usr/lib/libcrypto.so.10 && \  
wget ${SCALA_BINARY_DOWNLOAD_URL} && tar -zxvf
${SCALA_BINARY_ARCHIVE_NAME}.tgz -C /usr/local/ && \  
wget ${SBT_BINARY_DOWNLOAD_URL} && tar -zxvf ${SBT_BINARY_ARCHIVE_NAME}.tgz -C
/usr/local/ && \  
wget ${SPARK_BINARY_DOWNLOAD_URL} && tar -zxvf
${SPARK_BINARY_ARCHIVE_NAME}.tgz -C /usr/local/ && \  
cd /usr/local/ && \  
ln -s sbt-launcher-packaging-${SBT_VERSION} sbt && \  
ln -s ${SCALA_BINARY_ARCHIVE_NAME} scala && \  
ln -s ${SPARK_BINARY_ARCHIVE_NAME} spark && \  
cp spark/conf/log4j.properties.template spark/conf/log4j.properties && \  
sed -i -e s/WARN/ERROR/g spark/conf/log4j.properties && \  
sed -i -e s/INFO/ERROR/g spark/conf/log4j.properties  
# We will be running our Spark jobs as `root` user.  
USER root  
  
# Working directory is set to the home folder of `root` user.  
WORKDIR /root  
  
# Expose ports for monitoring.  
# SparkContext web UI on 4040 -- only available for the duration of the
application.  
# Spark master’s web UI on 8080.  
# Spark worker web UI on 8081.  
EXPOSE 4040 8080 8081 27017  
CMD ["/bin/bash"]  

