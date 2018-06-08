FROM kibana:4  
MAINTAINER Sergey Novikov <snov@snov.me>  
  
RUN gosu kibana /opt/kibana/bin/kibana plugin --install elastic/sense  
  
# See
https://www.elastic.co/guide/en/sense/current/installing.html#disable_discover  
# disable the standard kibana discovery, visualize & dashboard plugins  
# do not require a running Elasticsearch 2.0 instance  
RUN echo 'kibana.enabled: false' >> /opt/kibana/config/kibana.yml && \  
echo 'elasticsearch.enabled: false' >> /opt/kibana/config/kibana.yml  

