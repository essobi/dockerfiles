# This Dockerfile deploy a keystone container :  
# based on ubuntu:14.04, it runs the keystone source code from branch
stable/icehouse  
# it has to be linked to a mysql container named db-keystone :  
# -  
#  
FROM ubuntu:14.04  
MAINTAINER Francois Billant <fbillant@gmail.com>  
  
RUN echo "mysql-server mysql-server/root_password password neutre" | debconf-
set-selections  
RUN echo "mysql-server mysql-server/root_password_again password neutre" |
debconf-set-selections  
RUN apt-get update && apt-get -y install mysql-server  
  
ADD . /config  
  
EXPOSE 3306  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD cd /config && ./config.sh && ./run.sh  
  

