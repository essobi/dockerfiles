FROM logstash  
MAINTAINER Helain Schoonjans  
ADD config.sh /  
RUN chmod a+x config.sh  
  
CMD ["sh", "-c", "./config.sh && logstash -f config.conf"]  

