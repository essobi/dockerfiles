# supernova  
#  
# VERSION 1.0.0  
FROM debian:wheezy  
MAINTAINER Sven Müller <sven.mueller@commercetools.de>  
  
RUN apt-get update && apt-get install -y python-pip  
RUN pip install supernova rackspace-novaclient  
RUN pip install os-virtual-interfacesv2-python-novaclient-ext  
  
ENTRYPOINT ["supernova"]  

