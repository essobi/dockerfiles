FROM debian:jessie  
  
MAINTAINER Deon Thomas "Deon.Thomas.GY@gmail.com"  
ENV LANG C.UTF-8  
RUN apt-get update  
RUN apt-get install -y twms  
ADD twms.conf /etc/twms/twms.conf  
  
EXPOSE 8080  
CMD ["/usr/bin/twms"]  
  

