FROM ubuntu:latest  
MAINTAINER Erik van der Valk <erik.van.der.valk@fontoxml.com>  
MAINTAINER Martin Middel <martin.middel@fontoxml.com>  
MAINTAINER Stef Busking <stef.busking@fontoxml.com>  
  
# Update apt-get  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get dist-upgrade -y && \  
apt-get install -y build-essential curl git && \  
apt-get autoremove -y  
  
COPY ./src/root/.ssh /root/.ssh  

