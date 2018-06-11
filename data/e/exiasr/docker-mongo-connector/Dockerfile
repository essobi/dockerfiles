#This will prepare a elasticsearch node with mongo-connector enabled  
FROM python:3.4.3  
MAINTAINER michaellin@ualberta.ca  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TZ America/Edmonton  
  
# Installing Mongo Connector which will connect MongoDB and Elasticsearch  
RUN pip install 'mongo-connector[elastic5]' 'elastic2-doc-manager[elastic5]'  
  
COPY startup.sh /tmp/  
  
COPY mongo /usr/bin/  
RUN chmod a+x /usr/bin/mongo  
  
VOLUME /data  
  
# Sample usage when no commands is given outside  
CMD ["/bin/bash", "/tmp/startup.sh"]  

