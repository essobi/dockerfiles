FROM buildpack-deps:jessie-curl  
  
RUN apt-get update && apt-get install -y --no-install-recommends nano \  
&& rm -rf /var/lib/apt/lists/*  
  
MAINTAINER Morten Andersen <moander@outlook.com>  
  
RUN mkdir -p /usr/java \  
&& curl -sS https://storage.googleapis.com/mpub/java/jdk-8u65-linux-x64.gz \  
| tar -zxvC /usr/java  
  
ENV JAVA_HOME=/usr/java/jdk1.8.0_65  
  
ENV PATH=${JAVA_HOME}/bin:${PATH}  
  

