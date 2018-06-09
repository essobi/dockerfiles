FROM ubuntu:trusty  
  
MAINTAINER Tudor Marghidanu  
  
ENV NIFI_VERSION="0.6.1"  
ENV NIFI_HOME="/opt/nifi"  
RUN apt-get update; apt-get install -y build-essential \  
curl\  
openjdk-7-jdk  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/  
  
RUN mkdir -p ${NIFI_HOME}  
RUN curl -sL
http://apache.javapipe.com/nifi/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz
| tar zxvf - -C ${NIFI_HOME} \--strip-components=1  
  
EXPOSE 8080 8081  
WORKDIR ${NIFI_HOME}  
  
ENTRYPOINT [ "bin/nifi.sh" ]  
CMD [ "run" ]  

