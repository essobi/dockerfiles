FROM ubuntu:latest  
  
MAINTAINER Somesh yadav<somesh.yadav@imaginea.com>  
  
RUN apt-get -y update  
RUN echo "mysql-server mysql-server/root_password password root" | debconf-
set-selections  
RUN echo "mysql-server mysql-server/root_password_again password root" |
debconf-set-selections  
RUN apt-get install -y mysql-client mysql-server  
  
VOLUME ["/data"]  
  
ADD my.cnf /etc/mysql/my.cnf  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 3306  
CMD ["/run.sh"]  

