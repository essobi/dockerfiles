FROM java:8  
MAINTAINER Joe Friedl <joe@joefriedl.net>  
  
env KAFKA_VERSION 0.8.2.2  
env SCALA_VERSION 2.11  
COPY install.sh /opt/install.sh  
RUN chmod +x /opt/install.sh  
RUN /opt/install.sh  
  
WORKDIR /opt/kafka/  
COPY entrypoint.sh .  
RUN chmod +x entrypoint.sh  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 9092  
EXPOSE 2181  
ENTRYPOINT ["./entrypoint.sh"]  

