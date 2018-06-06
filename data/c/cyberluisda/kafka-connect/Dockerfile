FROM openshine/kafka:0.11.0.0  
  
MAINTAINER Luis David Barrios Alfonso (cyberluisda@gmail.com)  
  
#Netcat tools (need by logstash log4j output)  
RUN apt-get update && apt-get install -y --no-install-recommends netcat && rm
-rf /var/lib/apt/lists/*  
  
ADD files/kafka-connect.sh /bin/  
RUN chmod a+x /bin/kafka-connect.sh  
  
VOLUME /usr/lib/kafka/connect-extra /etc/kafka-connect  
  
ENV CLASSPATH /usr/lib/kafka/connect-extra/*  
  
EXPOSE 8083  
  
ENTRYPOINT ["/bin/kafka-connect.sh"]  
CMD ["--help"]  

