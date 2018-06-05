FROM openjdk:8  
MAINTAINER Rafal Liwoch <rafal.liwoch@gmail.com>  
## credits to Prashanth Babu https://github.com/P7h/docker-spark  
# Scala related variables.  
ARG SCALA_VERSION=2.12.2  
ARG SCALA_BINARY_ARCHIVE_NAME=scala-${SCALA_VERSION}  
ARG
SCALA_BINARY_DOWNLOAD_URL=http://downloads.lightbend.com/scala/${SCALA_VERSION}/${SCALA_BINARY_ARCHIVE_NAME}.tgz  
  
# SBT related variables.  
ARG SBT_VERSION=0.13.15  
ARG SBT_BINARY_ARCHIVE_NAME=sbt-$SBT_VERSION  
ARG SBT_BINARY_DOWNLOAD_URL=https://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/${SBT_BINARY_ARCHIVE_NAME}.tgz  
  
# Spark related variables.  
ARG SPARK_VERSION=2.2.1  
ARG SPARK_BINARY_ARCHIVE_NAME=spark-${SPARK_VERSION}-bin-without-hadoop  
ARG
SPARK_BINARY_DOWNLOAD_URL=http://apache.mirror.anlx.net/spark/spark-${SPARK_VERSION}/${SPARK_BINARY_ARCHIVE_NAME}.tgz  
  
# Hadoop related variables.  
ARG HADOOP_VERSION=2.9.0  
ARG HADOOP_BINARY_ARCHIVE_NAME=hadoop-${HADOOP_VERSION}  
ARG
HADOOP_BINARY_DOWNLOAD_URL=http://mirrors.ukfast.co.uk/sites/ftp.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/${HADOOP_BINARY_ARCHIVE_NAME}.tar.gz  
ARG HADOOP_DIR=/usr/local/hadoop  
  
# Configure env variables for Scala, SBT and Spark.  
# Also configure PATH env variable to include binary folders of Java, Scala,
SBT and Spark.  
ENV SCALA_HOME /usr/local/scala  
ENV SBT_HOME /usr/local/sbt  
ENV SPARK_HOME /usr/local/spark  
  
ENV PATH
$JAVA_HOME/bin:$SCALA_HOME/bin:$SBT_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH  
  
# Download, uncompress and move all the required packages and libraries to
their corresponding directories in /usr/local/ folder.  
RUN apt-get -yqq update && \  
apt-get install -yqq vim screen tmux nano && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
wget -qO - ${SCALA_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \  
wget -qO - ${SBT_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \  
wget -qO - ${SPARK_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \  
wget -qO - ${HADOOP_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \  
cd /usr/local/ && \  
ln -s ${SCALA_BINARY_ARCHIVE_NAME} scala && \  
ln -s ${SPARK_BINARY_ARCHIVE_NAME} spark && \  
ln -s ${HADOOP_BINARY_ARCHIVE_NAME} hadoop && \  
cp spark/conf/log4j.properties.template spark/conf/log4j.properties && \  
sed -i -e s/WARN/ERROR/g spark/conf/log4j.properties && \  
sed -i -e s/INFO/ERROR/g spark/conf/log4j.properties  
  
# Setup Hadoop  
RUN cd /usr/local/ && \  
chmod +x hadoop/bin/hadoop  
  
## Finally setup link between spark and hadoop's classpath  
# Copy script to produce hadoop env vars  
COPY sourceHadoopVars.sh /tmp/  
# Run script to setup env vars  
RUN /tmp/sourceHadoopVars.sh  
  
# Remove documentation - it's 400MB  
RUN rm -rf /usr/local/hadoop-${HADOOP_VERSION}/share/doc/  
  
# We will be running our Spark jobs as `root` user.  
USER root  
  
# Working directory is set to the home folder of `root` user.  
WORKDIR /root  
  
# Expose ports for monitoring.  
# SparkContext web UI on 4040 -- only available for the duration of the
application.  
# Spark master’s web UI on 8080.  
# Spark worker web UI on 8081.  
EXPOSE 4040 8080 8081  
CMD ["/bin/bash"]  

