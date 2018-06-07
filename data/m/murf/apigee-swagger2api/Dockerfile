FROM node:latest  
  
MAINTAINER Mikael@murf.se  
RUN npm install -g swagger2api  
  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh  
VOLUME /tmp:/tmp  
  
ENTRYPOINT ["/run.sh"]

