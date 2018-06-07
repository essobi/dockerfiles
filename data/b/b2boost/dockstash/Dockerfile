FROM logstash  
MAINTAINER Helain Schoonjans  
ADD config.sh /  
RUN chmod a+x config.sh  
RUN mkdir /opt/logstash/bin/patterns  
ADD custom_patterns /opt/logstash/bin/patterns/  
  
CMD ["sh", "-c", "./config.sh && logstash -f config.conf 2>&1 | tee
/var/log/dockstash.log"]

