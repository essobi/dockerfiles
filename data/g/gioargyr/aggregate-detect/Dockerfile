#####################################  
# Docker for BoostedImageAggregator #  
# BigDataEurope #  
# #  
# spark 1.6.2 #  
# maven 3.0.5 #  
# git 1.9.1 #  
# tomcat 8.0.23 #  
#####################################  
  
  
FROM java:8  
  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
# INSTALLING THE SPARK-APP PART  
COPY bde-spark.css /css/org/apache/spark/ui/static/timeline-view.css  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.2-bin-hadoop2.6.tgz \  
&& tar -xvzf spark-1.6.2-bin-hadoop2.6.tgz \  
&& mv spark-1.6.2-bin-hadoop2.6 spark \  
&& rm spark-1.6.2-bin-hadoop2.6.tgz \  
&& cd /css \  
&& jar uf /spark/lib/spark-assembly-1.6.2-hadoop2.6.0.jar
org/apache/spark/ui/static/timeline-view.css \  
&& cd /  
  
# INSTALLING THE IMAGE-AGGREGATOR WEB-SERVICE  
ENV PORT 8080  
ENV TOMCAT_MAJOR_VERSION 8  
ENV TOMCAT_MINOR_VERSION 8.0.23  
  
# INSTALL PREREQUISITIES  
RUN apt-get update && \  
apt-get install -y \  
maven \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# DOWNLOAD AND BUILD THE SPARK-APP  
RUN git clone https://github.com/big-data-europe/pilot-sc7-change-detector.git
&& \  
cd pilot-sc7-change-detector && \  
git checkout d0b25181fb515af3c903e39268f795546c9e2d5a && \  
mvn package  
  
RUN mkdir /spark-app && \  
mkdir /result && \  
cp /pilot-sc7-change-detector/target/changedetector-0.0.1-SNAPSHOT-
allinone.jar /spark-app  
  
# INSTALL TOMCAT  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* tomcat  
  
# DOWNLOAD AND BUILD THE IMAGE-AGGREGATOR-WS  
RUN git clone https://github.com/big-data-europe/pilot-sc7-image-
aggregator.git && \  
cd pilot-sc7-image-aggregator && \  
git checkout e47768fb7223193b2e6000b9140bc31b6339e04d && \  
mvn package  
  
RUN mkdir /images && \  
mkdir /resources && \  
cp /pilot-sc7-image-aggregator/target/*.war /tomcat/webapps  
  
ADD create_tomcat_admin_user.sh /create_tomcat_admin_user.sh  
ADD imgagg.sh /imgagg.sh  
ADD runchangedet.sh /runchangedet.sh  
ADD test.txt /test.txt  
ADD id.txt /resources  
RUN chmod +x /*.sh  
  
EXPOSE $PORT  
CMD ["/bin/bash", "/imgagg.sh"]  

