FROM thomaswelton/ubuntu  
  
MAINTAINER thomaswelton  
  
# Install mysql server  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server  
  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD run.sh /run.sh  
  
EXPOSE 3306  
CMD ["/bin/bash", "/run.sh"]  

