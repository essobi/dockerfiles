# dbninja installation  
#  
# VERSION 1.0  
#  
FROM ubuntu:trusty  
  
MAINTAINER Heimo Müller  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -qy mysql-client-5.6 apache2 libapache2-mod-php5
php5-mysql wget  
ADD start.sh /data/  
ADD install.sh /data/  
RUN chmod 755 /data/*.sh  
RUN /data/install.sh  
  
EXPOSE 80  
CMD ["/data/start.sh"]

