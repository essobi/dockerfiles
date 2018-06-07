FROM elasticsearch:5.5.0  
  
USER root  
RUN apt-get update  
RUN apt-get install -y dnsutils  
COPY es-docker /usr/share/elasticsearch/bin/  
  
USER elasticsearch  
CMD /usr/share/elasticsearch/bin/es-docker

