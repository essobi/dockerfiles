FROM busybox:latest  
  
VOLUME /fuseki/configuration  
  
ADD ./configuration /shippedConfig  
RUN mkdir -p /fuseki/configuration  
  
CMD cp /shippedConfig/* /fuseki/configuration

