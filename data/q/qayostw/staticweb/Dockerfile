FROM ubuntu:14.04  
#New owner  
MAINTAINER Quinn Yost <qyost@discover.com>  
  
RUN apt-get update  
RUN apt-get install -y netcat  
RUN echo 'Hi, I am in your container' \  
>/tmp/index.html  
  
CMD [ "netcat", "-l", "-p 8080 < /tmp/index.html;" ]  
  
EXPOSE 8080  

