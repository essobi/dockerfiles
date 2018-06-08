FROM openjdk:8u131-jdk-alpine  
  
ENV SPARK_HOME /usr/local  
RUN apk add \--no-cache --update bash wget && \  
mkdir -p "${SPARK_HOME}" && \  
wget -qO - --no-check-certificate
"https://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz" | tar xz
-C ${SPARK_HOME} \--strip-components=1 && \  
apk del wget  

