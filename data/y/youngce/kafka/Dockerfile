FROM youngce/oracle-java:1.8.0_51  
RUN export http_proxy="http://10.57.35.31:8080"  
RUN yum -y update  
RUN yum -y install tar telnet  
  
##KAFKA  
ENV SCALA_VERSION 2.10  
ENV KAFKA_VERSION 0.8.2.1  
ENV KAFKA_PKG_NAME kafka_$SCALA_VERSION-$KAFKA_VERSION  
WORKDIR /root  
  
RUN wget
http://ftp.mirror.tw/pub/apache/kafka/$KAFKA_VERSION/$KAFKA_PKG_NAME.tgz &&
tar -xzf $KAFKA_PKG_NAME.tgz  
  
WORKDIR /root/$KAFKA_PKG_NAME  
ADD config config  
ADD start.sh /root/start.sh  
RUN chmod 777 /root/start.sh  
EXPOSE 9092 2181  
CMD /root/start.sh  

