# Based on https://github.com/jacksoncage/salt-docker  
FROM ubuntu:14.04  
MAINTAINER Marian Zange <marian@crashpad.io>  
  
ENV SALT_VERSION v2015.8.0rc5  
  
# Download required packages  
RUN apt-get update  
RUN apt-get install -y wget python-software-properties software-properties-
common  
  
# Download and install SaltStack  
RUN wget -O install_salt.sh https://bootstrap.saltstack.com  
RUN sudo sh install_salt.sh -P git $SALT_VERSION; exit 0  
  
# Clean temporary files  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD etc/master /etc/salt/master  
ADD etc/minion /etc/salt/minion  
ADD etc/reactor /etc/salt/master.d/reactor  
  
EXPOSE 4505 4506  
ADD run.sh /run.sh  
CMD ["bash", "run.sh"]

