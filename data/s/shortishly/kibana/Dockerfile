FROM centos  
  
MAINTAINER Peter Morgan <peter.james.morgan@gmail.com>  
  
ENV KIBANA_VERSION 4.0.2  
RUN yum -y update && yum -y install \  
curl \  
tar  
  
RUN yum clean all  
  
RUN curl
https://download.elastic.co/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz
| tar -xzC /opt -f -  
  
ENV PATH /opt/kibana-${KIBANA_VERSION}-linux-x64/bin:$PATH  
ENTRYPOINT kibana --elasticsearch
http://${ELASTICSEARCH_PORT_9200_TCP_ADDR}:${ELASTICSEARCH_PORT_9200_TCP_PORT}  
EXPOSE 5601  

