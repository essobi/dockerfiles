FROM ubuntu:16.04  
MAINTAINER Chris Weyl <cweyl@alumni.drew.edu>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
C2079EE53D4B33595B07BDA9FE1FFCE65CB95493 && \  
echo "deb http://ppa.launchpad.net/vincent-c/ponysay/ubuntu xenial main" >>
/etc/apt/sources.list  
  
RUN \  
apt-get update && \  
apt-get -y install ponysay && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT [ "/usr/bin/ponysay" ]  

