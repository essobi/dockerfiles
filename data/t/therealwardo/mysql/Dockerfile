FROM ubuntu:12.04  
MAINTAINER Matt Ward  
  
RUN \  
apt-get update && \  
apt-get -y install mysql-server  
  
ADD startup.sh /opt/mysql-startup.sh  
  
EXPOSE 3306  
CMD ["/bin/bash", "/opt/mysql-startup.sh"]  

