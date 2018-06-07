FROM ubuntu:14.04  
MAINTAINER Dimitry Ushakov <dimitry.ushakov@rackspace.com>  
  
RUN apt-get install -y wget  
RUN wget -O - http://repo.openrepose.org/debian/pubkey.gpg | apt-key add - &&
echo "deb http://repo.openrepose.org/debian stable main" >
/etc/apt/sources.list.d/openrepose.list  
RUN apt-get update && apt-get install -y repose-valve=7.3.0.0 repose-filter-
bundle=7.3.0.0 repose-extensions-filter-bundle=7.3.0.0  
  
VOLUME /etc/repose  
WORKDIR /etc/repose  
USER repose  
  
RUN touch /var/log/repose/current.log  
  
USER root  
  
EXPOSE 8080 9777  
CMD service repose-valve start && tail -f /var/log/repose/current.log  
  

