FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
  
RUN \  
apt-get update && \  
apt-get install -y curl openjdk-6-jre-headless && \  
curl -O
https://downloads.mesosphere.io/master/ubuntu/14.04/mesos_0.20.1-1.0.ubuntu1404_amd64.deb
&& \  
dpkg --unpack mesos_0.20.1-1.0.ubuntu1404_amd64.deb && \  
apt-get install -f -y && \  
rm mesos_0.20.1-1.0.ubuntu1404_amd64.deb && \  
apt-get clean  

