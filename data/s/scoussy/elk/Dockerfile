FROM phusion/baseimage  
  
### install elasticsearch and logstash  
RUN apt-get update -qq && apt-get install -qqy curl  
  
RUN curl https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -  
RUN add-apt-repository "deb
http://packages.elastic.co/elasticsearch/2.x/debian stable main"  
RUN add-apt-repository "deb http://packages.elastic.co/logstash/2.2/debian
stable main"  
RUN add-apt-repository "deb http://packages.elastic.co/kibana/4.4/debian
stable main"  
  
RUN apt-get update -qq && apt-get install -qqy openjdk-7-jdk elasticsearch
logstash kibana  
  
ADD ./elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
  
ADD ./logstash-tcp-input.conf /etc/logstash/conf.d/logstash-tcp-input.conf  
ADD ./logstash-udp-input.conf /etc/logstash/conf.d/logstash-udp-input.conf  
ADD ./logstash-gelf-input.conf /etc/logstash/conf.d/logstash-gelf-input.conf  
ADD ./logstash-beats-input.conf /etc/logstash/conf.d/logstash-beats-input.conf  
ADD ./logstash-elasticsearch-output.conf /etc/logstash/conf.d/logstash-
elasticsearch-output.conf  
  
### install start-up script  
RUN mkdir /etc/service/elk  
ADD ./run.sh /etc/service/elk/run  
RUN chmod +x /etc/service/elk/run  
  
### volume with elasticsearch-data  
VOLUME ["/var/lib/elasticsearch/elasticsearch"]  
  
### start up everthing  
EXPOSE 9200 4560 4570/udp 12201 5044 5601  
CMD [ "/etc/service/elk/run" ]  

