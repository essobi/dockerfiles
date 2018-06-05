#  
FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y cacti wget  
  
COPY cacti.sql /  
COPY run.sh /run.sh  
  
VOLUME [ "/var/log/", "/var/lib/mysql" , "/var/lib/cacti" ]  
  
EXPOSE 80  
ENTRYPOINT /run.sh  

