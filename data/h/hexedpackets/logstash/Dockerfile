FROM jruby:1.7  
MAINTAINER William Huba <hexedpackets@gmail.com>  
  
RUN apt-get update && apt-get install -y git  
  
RUN cd /opt && git clone https://github.com/elastic/logstash  
WORKDIR /opt/logstash  
RUN rake bootstrap  
  
ENV PATH $PATH:/opt/logstash/bin  

