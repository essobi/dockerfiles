FROM node:0.10.32  
MAINTAINER SequenceIQ  
  
ENV ST_PORT 3003  
RUN apt-get update  
RUN apt-get install -y curl unzip  
EXPOSE 3003  
ADD start.sh /status/  
  
CMD ["/status/start.sh"]  

