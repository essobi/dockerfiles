FROM centos:7  
MAINTAINER Aman Mangal <mangalaman93@gmail.com>  
  
# Install Java  
RUN yum -y \--setopt=tsflags=nodocs install java-1.8.0-openjdk && \  
yum clean all  
ENV JAVA_HOME=/usr/lib/jvm/jre  
  
# Download Spark  
ENV SPARK_VERSION=2.1.0  
ENV SPARK_DOWNLOAD_URL=http://www-
eu.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-
hadoop2.7.tgz  
RUN curl -o spark-$SPARK_VERSION-bin-hadoop2.7.tgz -SL $SPARK_DOWNLOAD_URL &&
\  
tar -xf spark-$SPARK_VERSION-bin-hadoop2.7.tgz && \  
mv spark-$SPARK_VERSION-bin-hadoop2.7 /opt/spark && \  
rm spark-$SPARK_VERSION-bin-hadoop2.7.tgz  
ENV SPARK_HOME=/opt/spark  

