# DOCKER-VERSION 1.2.0  
# VERSION 0.3  
FROM zooniverse/java  
MAINTAINER Edward Paget <ed@zooniverse.org>  
  
ENV KAFKA_VERSION 0.8.2.0  
ENV SCALA_VERSION 2.11  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y -q wget && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -q -O -
"http://www.mirrorservice.org/sites/ftp.apache.org/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz"
| \  
tar zx -C /opt/  
ADD start_kafka.sh /opt/start_kafka.sh  
RUN chmod +x /opt/start_kafka.sh  
  
EXPOSE 9092  
ENTRYPOINT ["./opt/start_kafka.sh"]  

