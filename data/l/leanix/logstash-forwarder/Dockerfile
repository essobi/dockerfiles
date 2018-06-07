FROM ubuntu:14.04  
MAINTAINER Andre Christ <andre.christ@leanix.net>  
  
RUN apt-get update  
RUN apt-get install -y golang git wget tar  
RUN mkdir -p /opt/logstash-forwarder  
RUN wget https://github.com/elasticsearch/logstash-
forwarder/archive/v0.4.0.tar.gz  
RUN tar zxvf v0.4.0.tar.gz -C /opt/logstash-forwarder --strip-components=1  
RUN cd /opt/logstash-forwarder/ && go build  
RUN apt-get remove -y wget git golang  
RUN apt-get autoremove -y  
  
# does not work  
RUN echo "172.31.16.115 logstash.acme.com" >> /etc/hosts  
  
CMD echo 172.31.16.115 logstash.acme.com >> /etc/hosts && /opt/logstash-
forwarder/logstash-forwarder -config /etc/logstash/forwarder.conf  

