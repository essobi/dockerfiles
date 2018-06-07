FROM jwilder/docker-gen:0.7.3  
MAINTAINER Nuts Project, LLC  
  
COPY docker-gen.conf /docker-gen.conf  
COPY templates/ /etc/docker-gen/templates  
  
ENTRYPOINT ["/usr/local/bin/docker-gen"]  

