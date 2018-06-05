FROM ubuntu:16.04  
MAINTAINER Love Nyberg "love.nyberg@lovemusic.se"  
ENV REFRESHED_AT 2016-01-20  
# Update system  
RUN apt-get update && \  
apt-get install -y wget curl dnsutils python-pip python-dev python-apt
software-properties-common dmidecode  
  
# Setup salt repo  
RUN wget -O -
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/2016.11/SALTSTACK-GPG-
KEY.pub | apt-key add - && \  
echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/2016.11 xenial
main" > /etc/apt/sources.list.d/saltstack.list  
  
# Install salt master/minion/cloud/api  
RUN apt-get update && \  
apt-get install -y salt-master salt-minion \  
salt-cloud salt-api  
  
# DEPRECATED: https://groups.google.com/forum/#!msg/salt-
users/rmMWLSaw0RY/N5PGRqDkwQgJ  
# Setup halite  
# RUN pip install cherrypy docker-py halite  
# Add salt config files  
ADD etc/master /etc/salt/master  
ADD etc/minion /etc/salt/minion  
ADD etc/reactor /etc/salt/master.d/reactor  
  
# Expose volumes  
VOLUME ["/etc/salt", "/var/cache/salt", "/var/logs/salt", "/srv/salt"]  
  
# Exposing salt master and api ports  
EXPOSE 4505 4506 8080 8081  
# Add and set start script  
ADD start.sh /start.sh  
CMD ["bash", "start.sh"]  

