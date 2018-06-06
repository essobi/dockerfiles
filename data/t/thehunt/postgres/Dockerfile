FROM postgres:9.4  
MAINTAINER Peter Salanki <peter@salanki.st>  
  
RUN rm /docker-entrypoint.sh  
COPY docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
  
RUN mkdir -p /opt/baseconfig  
COPY baseconfig /opt/baseconfig  

