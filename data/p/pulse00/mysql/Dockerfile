FROM stackbrew/ubuntu:13.10  
MAINTAINER Robert Gruendler <r.gruendler@dubture.com>  
  
# install the package  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install mysql-server  
  
# Let other containers connect  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# expose the port  
EXPOSE 3306  
# add startup script and and run it  
ADD ./startup.sh /opt/startup.sh  
CMD ["/bin/bash", "/opt/startup.sh"]  
  

