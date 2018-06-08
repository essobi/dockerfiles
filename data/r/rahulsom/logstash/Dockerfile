FROM logstash:alpine  
MAINTAINER Rahul Somasunderam <rahul.som@gmail.com>  
  
RUN /usr/share/logstash/bin/logstash-plugin install logstash-filter-multiline  
  
VOLUME ["/local"]  
WORKDIR /local  

