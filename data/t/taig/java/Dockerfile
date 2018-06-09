FROM ubuntu:16.04  
MAINTAINER Niklas Klein "mail@taig.io"  
ENV JAVA_VERSION 8  
ENV JAVA_UPDATE 112  
ENV JAVA_BUILD 15  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
WORKDIR /root/  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y --no-install-recommends \  
wget \  
ca-certificates  
RUN apt-get clean  
  
RUN wget \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz  
RUN mkdir ./jdk/  
RUN tar xzf jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz -C ./jdk/
--strip-components 1  
RUN rm jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz  
  
ENV PATH $PATH:/root/jdk/bin  
ENV JAVA_HOME /root/jdk/

