FROM docker.elastic.co/elasticsearch/elasticsearch:5.4.1  
MAINTAINER Jaeger <JaegerCode@gmail.com>  
ADD ik /usr/share/elasticsearch/plugins/ik  
USER root  
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/plugins/ik  
USER elasticsearch  

