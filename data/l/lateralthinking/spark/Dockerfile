FROM openjdk:8-jre  
MAINTAINER Mariano Kamp <mariano.kamp@gmail.com>  
  
# Version  
ENV SPARK_VERSION=2.2.0  
# Set home  
ENV SPARK_HOME=/usr/local/spark-$SPARK_VERSION  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install \  
-yq --no-install-recommends \  
netcat telnet vim\  
&& rm -rf /var/lib/apt/lists/*  
  
# https://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz  
# Install Spark  
RUN mkdir -p "${SPARK_HOME}" \  
&& export ARCHIVE=spark-$SPARK_VERSION-bin-hadoop2.7.tgz && export
DOWNLOAD_PATH=apache/spark/spark-$SPARK_VERSION/$ARCHIVE \  
&& curl -sSL http://mirror.dkd.de/$DOWNLOAD_PATH | \  
tar -xz -C $SPARK_HOME \--strip-components 1 \  
&& rm -rf $ARCHIVE  
  
ENV PATH=$PATH:$SPARK_HOME/bin  
  
# Ports  
#EXPOSE 6066 7077 8080 8081  

