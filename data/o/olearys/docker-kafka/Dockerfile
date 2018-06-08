FROM java:7  
MAINTAINER Kurt Greiner  
  
ENV KF_VERSION 0.8.2.2  
RUN wget -qO-
http://ftp.unicamp.br/pub/apache/kafka/0.8.2.2/kafka_2.11-${KF_VERSION}.tgz |
tar xzf - -C /opt  
RUN mv /opt/kafka_2.11-${KF_VERSION} /opt/kafka  
  
EXPOSE 9092  
VOLUME ["/data/kafka"]  
  
ADD server.properties /opt/kafka/config/server.properties  
ADD start /opt/kafka/bin/start  
  
CMD ["/opt/kafka/bin/start"]  

