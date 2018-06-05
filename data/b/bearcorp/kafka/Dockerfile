FROM openjdk  
  
LABEL maintainer "jcm.rodgers@gmail.com"  
  
COPY start_queue.sh /start_queue.sh  
  
RUN wget
http://www.mirrorservice.org/sites/ftp.apache.org/kafka/0.10.1.0/kafka_2.11-0.10.1.0.tgz
&& \  
tar xfz kafka_2.11-0.10.1.0.tgz && \  
rm kafka_2.11-0.10.1.0.tgz  
  
COPY config/server.properties /kafka_2.11-0.10.1.0/config/server.properties  
  
# convert windows line endings to unix  
RUN perl -pi -e's/\015\012/\012/g' start_queue.sh  
RUN perl -pi -e's/\015\012/\012/g'
/kafka_2.11-0.10.1.0/config/server.properties  
  
RUN chmod +x /start_queue.sh  
  
# kafka  
EXPOSE 9092  
# zookeeper  
EXPOSE 2128  
CMD ["/start_queue.sh"]  

