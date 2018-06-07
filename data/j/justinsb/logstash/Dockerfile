FROM ubuntu:trusty  
  
RUN apt-get update  
RUN apt-get install -y wget openjdk-7-jre-headless  
RUN cd /opt && wget
https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz &&
tar zxf logstash-1.4.2.tar.gz && rm logstash-1.4.2.tar.gz  
RUN ln -s /opt/logstash-1.4.2 /opt/logstash  
ADD run.sh /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
RUN rm -rf /tmp/*  
  
EXPOSE 514  
EXPOSE 9200  
EXPOSE 9292  
EXPOSE 9300  
CMD ["/usr/local/bin/run"]  

