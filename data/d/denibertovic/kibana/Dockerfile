# Kibana  
#  
# Explore & Visualize Your Data  
#  
# VERSION 4.0.1  
FROM debian:jessie  
MAINTAINER Deni Bertovic "me@denibertovic.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y ca-certificates wget  
  
RUN wget
https://download.elasticsearch.org/kibana/kibana/kibana-4.0.1-linux-x64.tar.gz
-O /tmp/kibana.tar.gz 2> /dev/null  
  
RUN tar zxvf /tmp/kibana.tar.gz -C /tmp && mv /tmp/kibana-4.0.1-linux-x64
/kibana && rm -rf /tmp/*  
  
RUN mkdir /logs  
  
ADD start_kibana.sh /usr/local/bin/start_kibana.sh  
RUN chmod +x /usr/local/bin/start_kibana.sh  
  
VOLUME ["/kibana/config", "/logs"]  
  
CMD ["/usr/local/bin/start_kibana.sh"]  
  

