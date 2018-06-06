# Builds a base docker image for the Confluent stream platform. It doesn't  
# start up any particular service, just installs the platform. Other images  
# inherit from this image to start up a particular service.  
FROM debian:8.2  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV SCALA_VERSION="2.11.7"  
ENV JAVA_VERSION="8"  
ENV CP_VERSION="2.0.1"  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list &&\  
apt-get update &&\  
apt-get -y upgrade &&\  
apt-get -y install \  
apt-utils \  
bash \  
curl \  
openjdk-${JAVA_VERSION}-jre-headless &&\  
curl -sSL http://packages.confluent.io/deb/${CP_VERSION%.*}/archive.key | apt-
key add - &&\  
if [ "${CP_VERSION}" = "1.0.1" ]; then echo "deb [arch=all]
http://packages.confluent.io/deb/${CP_VERSION%.*} stable main" >>
/etc/apt/sources.list.d/confluent.list ;\  
else echo "deb [arch=amd64] http://packages.confluent.io/deb/${CP_VERSION%.*}
stable main" >> /etc/apt/sources.list.d/confluent.list ; fi &&\  
apt-get update &&\  
apt-get -y install confluent-platform-${SCALA_VERSION}  

