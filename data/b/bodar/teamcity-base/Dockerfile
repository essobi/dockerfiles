# docker run bodar/docker-java8  
FROM ubuntu:wily  
  
MAINTAINER Dan Bodart <dan@bodar.com>  
  
RUN apt-get update -qq && \  
apt-get install -qqy \  
curl wget git mercurial unzip gettext-base ca-certificates jq s3cmd \  
\--no-install-recommends  
  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LANGUAGE en_GB:en  
ENV LC_ALL en_GB.UTF-8  
ENV JDK_18 /opt/java/jdk1.8  
ENV JDK_18_URL http://download.oracle.com/otn-
pub/java/jdk/8u73-b02/jdk-8u73-linux-x64.tar.gz  
RUN mkdir -p ${JDK_18} && \  
curl -jkL -H "Cookie: oraclelicense=accept-securebackup-cookie" ${JDK_18_URL}
| \  
tar -C ${JDK_18} -xz --strip 1  
  
ENV JDK_17 /opt/java/jdk1.7  
ENV JDK_17_URL http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz  
RUN mkdir -p ${JDK_17} && \  
curl -jkL -H "Cookie: oraclelicense=accept-securebackup-cookie" ${JDK_17_URL}
| \  
tar -C ${JDK_17} -xz --strip 1  
  
ENV JAVA_HOME ${JDK_18}  
ENV PATH ${JAVA_HOME}/bin:${PATH}  
  
RUN curl -jkL
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz | \  
tar -C /usr/local/bin -xz  

