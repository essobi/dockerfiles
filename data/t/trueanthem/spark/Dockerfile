  
FROM debian:wheezy  
  
LABEL VERSION=0.0.1  
  
RUN apt-get update && \  
apt-get install -y \  
openjdk-7-jre-headless \  
scala \  
curl \  
wget  
  
RUN apt-get remove -y \  
scala-library \  
scala  
  
# install scala 2.10.5  
RUN cd /tmp && \  
wget -q http://downloads.typesafe.com/scala/2.10.5/scala-2.10.5.deb && \  
dpkg -i scala-2.10.5.deb && \  
rm -f scala-2.10.5.deb  
  
LABEL SPARK_BUILD=1.4.0  
  
RUN mkdir -p /spark && \  
wget -qO- http://d3kbcqa49mib13.cloudfront.net/spark-1.4.0-bin-hadoop2.4.tgz |
tar -xz -C /spark --strip-components=1  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64  
RUN update-alternatives --set java /usr/lib/jvm/java-7-openjdk-
amd64/jre/bin/java  

