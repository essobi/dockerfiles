FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.7  
MAINTAINER Uwe Kleinmann <u.kleinmann@kellerkinder.de>  
  
ADD templates/elasticsearch.yml /usr/share/elasticsearch/config/  
USER root  
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml  
USER elasticsearch  
  
CMD ["/bin/bash", "bin/es-docker"]  

