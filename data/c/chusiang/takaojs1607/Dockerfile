# Dockerfile for building image that contains software stack provisioned by
Ansible.  
#  
# USAGE:  
# $ docker build -t chusiang/takaojs1607 . | tee output.log  
#  
# Version 1.0  
#  
# pull base image  
#  
# - OS: Ubuntu 15.04  
# - only support angular-seed.  
#  
FROM selenium/standalone-chrome-debug:2.48.2  
MAINTAINER Chu-Siang Lai <chusiang.lai@gmail.com>  
  
# fix policy-rc.d for Docker  
# @see http://www.monblocnotes.com/node/2057  
# @see http://askubuntu.com/a/365912  
RUN sed -i -e 's/exit\s\s*101/exit 0/' /usr/sbin/policy-rc.d  
  
# Deploy node.js.  
RUN apt-get update ;\  
apt-get install -y git curl make npm node.js ;\  
npm install -g n ;\  
n 5.12.0  
# Deploy angular-seed.  
RUN sudo su seluser -c \  
'git clone https://github.com/angular/angular-seed.git ~/angular-seed' ;\  
chown -R seluser:seluser /home/seluser/angular-seed/ ;\  
cd /home/seluser/angular-seed/ ;\  
sudo su seluser -c 'npm install'  
# VNC  
EXPOSE 5900  

