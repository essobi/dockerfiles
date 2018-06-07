FROM ubuntu:16.04  
MAINTAINER pykiss  
  
LABEL version="2.1"  
  
RUN apt-get update -y  
RUN apt-get install curl -y  
RUN apt-get install nodejs -y  
RUN apt-get install npm -y  
  
WORKDIR /meteor  
COPY start.sh /  
  
ENTRYPOINT ["bash", "/start.sh"]  
  
CMD []  

