FROM famersbs/delauncher_base  
MAINTAINER Sean <famersbs@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y openjdk-7-jre-headless python  
  
# https://www.apache.org/mirrors/dist.html  
RUN curl -fL
http://apache.mirror.digitalpacific.com.au/zookeeper/stable/zookeeper-3.4.6.tar.gz
| tar xzf - -C /opt && \  
mv /opt/zookeeper-3.4.6 /opt/zookeeper  
  
ADD run.sh run.sh

