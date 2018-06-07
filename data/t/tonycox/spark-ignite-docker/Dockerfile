# Configuration of Java-8 Spark-1.6.3-hadoop-2.6 on top of ubuntu  
#  
# Author Anton Solovev  
FROM ubuntu:16.04  
LABEL maintainer "https://github.com/tonycox"  
LABEL version="1.0"  
  
# To skip interactive events while building  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Temp vars  
ARG SPARK_VERSION=spark-1.6.3  
ARG HADOOP_VERSION=hadoop2.6  
ARG IGNITE_VERSION=1.8.0  
# Install  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y curl git unzip vim wget apt-utils software-properties-
common && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Set environment variables.  
ENV HOME /root  
  
# Install Java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | \  
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# RUN apt-get-install -y python3 python3-setuptools python3-pip  
# ENV PYTHONHASHSEED 1  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Download Spark package  
ADD
http://d3kbcqa49mib13.cloudfront.net/${SPARK_VERSION}-bin-${HADOOP_VERSION}.tgz
/tmp/  
  
# Download ignite  
ADD http://apache-mirror.rbc.ru/pub/apache//ignite/${IGNITE_VERSION}/apache-
ignite-fabric-${IGNITE_VERSION}-bin.zip /tmp/  
  
RUN mkdir -p /opt/  
  
# Unpack spark into /opt and set SPARK_HOME  
RUN tar -xzf /tmp/${SPARK_VERSION}-bin-${HADOOP_VERSION}.tgz -C /opt/  
ENV SPARK_HOME /opt/${SPARK_VERSION}-bin-${HADOOP_VERSION}  
  
# Unpack ignite /opt and set IGNITE_HOME  
RUN unzip /tmp/apache-ignite-fabric-${IGNITE_VERSION}-bin.zip -d /opt/  
ENV IGNITE_HOME /opt/apache-ignite-fabric-${IGNITE_VERSION}-bin  
  
ENV PATH $PATH:${SPARK_HOME}/sbin/:${SPARK_HOME}/bin:${IGNITE_HOME}/bin

