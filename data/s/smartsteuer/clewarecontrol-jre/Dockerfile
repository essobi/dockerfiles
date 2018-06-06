FROM smartsteuer/clewarecontrol:latest  
MAINTAINER Eike Hirsch <eike.hirsch@smartsteuer.de>  
  
# install java  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jre-headless  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

