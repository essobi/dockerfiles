FROM ubuntu:16.04  
MAINTAINER Jaeger <JaegerCode@gmail.com>  
  
ADD start.sh /  
  
USER root  
  
RUN apt-get update && apt-get install software-properties-common vim -y  
  
RUN chmod +x /start.sh  
  
CMD /start.sh  
  

