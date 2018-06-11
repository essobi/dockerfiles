FROM ubuntu:trusty  
MAINTAINER Vasyl Purchel <vasyl.purchel@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y wget openjdk-7-jre-headless \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget http://www.eu.apache.org/dist/kafka/0.9.0.1/kafka_2.10-0.9.0.1.tgz \  
&& wget http://www.eu.apache.org/dist/kafka/0.9.0.1/kafka_2.10-0.9.0.1.tgz.md5
\  
&& md5sum kafka_2.10-0.9.0.1.tgz \  
&& tar xzf kafka_2.10-0.9.0.1.tgz -C /opt \  
&& mv /opt/kafka_2.10-0.9.0.1 /opt/kafka  
  
ADD server.properties /opt/kafka/config/  
  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/kafka/bin
\  
KAFKA_HOME=/opt/kafka \  
KAFKA_CONFIG_FILE=/opt/kafka/config/server.properties  
  
ADD docker-entry-point.sh /opt/kafka/  
ENTRYPOINT ["/opt/kafka/docker-entry-point.sh"]  
CMD ["kafka-server-start.sh", "/opt/kafka/config/server.properties"]  

