  
FROM ubuntu:14.04  
FROM tomcat:8.0  
MAINTAINER jabajaj  
EXPOSE 8080  
Run apt-get update  
Run apt-get install -y curl  
Run apt-get install -y vim  
  
# Fix sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y git build-essential curl wget software-properties-common  
  
COPY System.war /usr/local/tomcat/webapps/  
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]  

