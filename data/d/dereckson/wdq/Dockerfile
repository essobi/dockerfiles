#  
# Docker image to install and compile WDQ  
#  
# WDQ is a software designed by Magnus Manske to offer an API  
# allowing claims search  
#  
FROM ubuntu:trusty  
MAINTAINER Sébastien Santoro <dereckson@espace-win.org>  
  
RUN apt-get update ; apt-get -y install git make g++ php5-cli libmysqlclient-
dev mysql-server libcurl4-openssl-dev  
RUN mkdir -p /opt && git clone
https://bitbucket.org/magnusmanske/wikidataquery.git /opt/wdq && cd /opt/wdq
&& make  
  
EXPOSE 80  
CMD ["init"]  

