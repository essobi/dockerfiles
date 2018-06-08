FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
#install ceilometer  
RUN apt-get -y update  
RUN apt-get install -y --force-yes mongodb-server  
  
EXPOSE 27017  
CMD ['usr/bin/mongod']  

