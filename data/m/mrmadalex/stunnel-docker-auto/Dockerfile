FROM ubuntu:latest  
MAINTAINER Alexander  
  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install stunnel4 -y  
  
VOLUME /etc/stunnel  
  
EXPOSE 443  
  
ENTRYPOINT ["/"]  
CMD ["stunnel"]  

