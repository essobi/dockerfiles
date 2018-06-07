#This will prepare a elasticsearch node with mongo-connector enabled  
FROM python:3.4.3  
LABEL maintainer "Florian Kinder <florian.kinder@fankserver.com>"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Installing Mongo Connector which will connect MongoDB and Elasticsearch  
RUN pip install 'mongo-connector[elastic5]' && \  
pip install 'elastic2-doc-manager[elastic5]'  
  
COPY entrypoint.sh /entrypoint.sh  
COPY mongo /usr/bin/  
  
VOLUME ["/data"]  
  
# Sample usage when no commands is given outside  
ENTRYPOINT ["/entrypoint.sh"]  

