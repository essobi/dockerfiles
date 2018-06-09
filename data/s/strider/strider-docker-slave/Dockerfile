# DOCKER-VERSION 1.0.0  
FROM ubuntu:14.04  
MAINTAINER Keyvan Fatehi <keyvanfatehi@gmail.com>  
  
RUN apt-get -y update  
  
# Node.js and Git are required  
RUN apt-get -y install nodejs npm git  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
# git wants this  
RUN locale-gen en_US.UTF-8  
  
# Setup workspace and user  
RUN adduser --home /home/strider --gecos "" strider  
RUN mkdir -p /home/strider/workspace  
RUN chown -R strider /home/strider  
  
# Get the slave  
RUN npm install -g strider-docker-slave@1.*.*  
  
# Install supervisord  
RUN apt-get -y install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
ADD write-to-file /usr/local/bin/  
ADD ssh.sh /home/strider/  
ENV GIT_SSH /home/strider/ssh.sh  
  
# Run the slave  
# Additional background services can be configured by adding  
# a supervisor config file to the config directory  
# (/etc/supervisor/conf.d/)  
CMD supervisord -c /etc/supervisor/supervisord.conf && su strider -c 'strider-
docker-slave'  
  
WORKDIR /home/strider/workspace  
ENV HOME /home/strider  
  
# Other packages that people might want:  
# - make  
# - build-essential  
# - python-dev  
# - default-jre-headless  
# - ruby  

