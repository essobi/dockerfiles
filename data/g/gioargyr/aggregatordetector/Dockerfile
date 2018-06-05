#####################################  
# Dockerfile for AggregatorDetector #  
# BigDataEurope #  
# #  
# java 1.8.0_11 #  
# maven 3.0.5 #  
# git 1.9.1 #  
# tomcat 8.0.23 #  
# spark 1.6.2 #  
#####################################  
FROM ubuntu:14.04  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
ENV PORT 8080  
ENV TOMCAT_MAJOR_VERSION 8  
ENV TOMCAT_MINOR_VERSION 8.0.23  
# INSTALL PREREQUISITIES  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
curl \  
maven \  
git \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# (NEW) JAVA8-INSTALLATION  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt update \  
&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections \  
&& apt install -y oracle-java8-installer  
  
# INSTALL SPARK  
RUN apt-get update \  
&& wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.2-bin-hadoop2.6.tgz \  
&& tar -xvzf spark-1.6.2-bin-hadoop2.6.tgz \  
&& mv spark-1.6.2-bin-hadoop2.6 spark \  
&& rm spark-1.6.2-bin-hadoop2.6.tgz \  
&& apt-get install -y libgfortran3  
  
# INSTALL TOMCAT  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz \  
&& wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - \  
&& tar zxf apache-tomcat-*.tar.gz \  
&& rm apache-tomcat-*.tar.gz \  
&& mv apache-tomcat* tomcat  
  
# DOWNLOAD AND BUILD subsetOperator  
RUN git clone -b subsetOperator https://github.com/big-data-europe/pilot-
sc7-change-detector.git \  
&& cd pilot-sc7-change-detector \  
&& mvn clean package  
  
RUN mkdir /javasparkapps \  
&& mkdir /snap \  
&& mv /pilot-sc7-change-detector/target/spark.test-0.0.1-SNAPSHOT-allinone.jar
/javasparkapps/subset.jar \  
&& rm -rf /pilot-sc7-change-detector  
  
# DOWNLOAD AND BUILD spark-ChangeDetector  
RUN git clone -b subsetIntegration https://github.com/big-data-europe/pilot-
sc7-change-detector.git \  
&& cd pilot-sc7-change-detector \  
&& mvn clean package  
  
RUN mkdir /cdlogs \  
&& mv /pilot-sc7-change-detector/target/changedetector-0.0.1-SNAPSHOT-
allinone.jar /javasparkapps/sparkchangedet.jar \  
&& rm -rf /pilot-sc7-change-detector  
  
# DOWNLOAD AND BUILD spark-DBScan  
RUN cd /cdlogs \  
&& git clone -b DBScan https://github.com/big-data-europe/pilot-sc7-change-
detector.git \  
&& cd pilot-sc7-change-detector \  
&& mvn clean package  
  
RUN mkdir /dbscanlogs \  
&& mv /cdlogs/pilot-sc7-change-detector/target/spark.test-0.0.1-SNAPSHOT-
allinone.jar /javasparkapps/sparkdbscan.jar \  
&& rm -rf /cdlogs/pilot-sc7-change-detector  
  
# DOWNLOAD AND BUILD image-aggregator service  
RUN git clone -b cdflow https://github.com/big-data-europe/pilot-sc7-image-
aggregator.git \  
&& cd pilot-sc7-image-aggregator \  
&& mvn clean package  
  
RUN cp /pilot-sc7-image-aggregator/target/*.war /tomcat/webapps \  
&& rm -rf pilot-sc7-image-aggregator  
  
ADD aggregatordetector.sh /aggregatordetector.sh  
ADD runsubset.sh /runsubset.sh  
ADD runchangedet.sh /runchangedet.sh  
ADD rundbscan.sh /rundbscan.sh  
  
RUN chmod +x /*.sh  
  
EXPOSE $PORT  
CMD ["/bin/bash", "/aggregatordetector.sh"]  

