FROM ubuntu:12.04  
MAINTAINER Arcus "http://arcus.io"  
RUN apt-get update  
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y wget mysql-
server  
ADD run.sh /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
EXPOSE 3306  
CMD ["/usr/local/bin/run"]  

