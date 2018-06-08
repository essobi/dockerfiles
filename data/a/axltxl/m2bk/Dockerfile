FROM python:3.3  
MAINTAINER Alejandro Ricoveri <alejandroricoveri@gmail.com>  
  
#  
# Upgrade packages  
#  
RUN apt-get update && apt-get upgrade -y && apt-get -y autoremove  
  
#  
# Install mongodb-tools  
#  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
> /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -y mongodb-org-tools  
  
#  
# Install m2bk  
#  
RUN pip install m2bk==0.3.1  
#  
# Set the m2bk executable as the entry point  
#  
ENTRYPOINT ["/usr/local/bin/m2bk"]  

