FROM node:0.10  
MAINTAINER Klaus Bittrich "aaukt@posteo.de"  
ENV JAVA_VERSION 7u65  
RUN apt-get update && apt-get install -y \  
openjdk-7-jdk="$JAVA_VERSION"* unzip wget libreoffice net-tools supervisor  
  
ENV ACTIVEMQ_VERSION 5.10.0  
RUN curl -SL "http://apache.openmirror.de/activemq/$ACTIVEMQ_VERSION/apache-
activemq-$ACTIVEMQ_VERSION-bin.tar.gz" -o activemq.tar.gz \  
&& curl -SL "https://www.apache.org/dist/activemq/$ACTIVEMQ_VERSION/apache-
activemq-$ACTIVEMQ_VERSION-bin.tar.gz.asc" -o activemq.tar.gz.asc \  
&& curl -SL "https://www.apache.org/dist/activemq/KEYS" -o KEYS \  
&& gpg --import KEYS \  
&& gpg --verify activemq.tar.gz.asc \  
&& mkdir -p /opt \  
&& tar zxvf activemq.tar.gz -C /opt \  
&& rm activemq.tar.gz activemq.tar.gz.asc KEYS \  
&& mv /opt/apache-activemq-$ACTIVEMQ_VERSION /opt/activemq  
  
RUN curl -SL "https://github.com/owncloud/format-filter-
server/archive/master.tar.gz" -o ffs.tar.gz \  
&& tar zxvf ffs.tar.gz -C /opt \  
&& rm ffs.tar.gz \  
&& mv /opt/format-filter-server-master /opt/ffs \  
&& cd /opt/ffs \  
&& npm install stomp uuid  
  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 16080  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "-n"]  

