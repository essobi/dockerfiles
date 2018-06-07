# This file describes how to build Plone into a runnable linux container with
all dependencies installed  
# To build:  
# 1) Install docker (http://docker.io)  
# 2) Run:  
# docker run -d <imageid>  
#  
# VERSION 0.3  
# DOCKER-VERSION 1.3.2  
from ubuntu:14.04  
MAINTAINER Gauthier C.  
run apt-get update  
run apt-get upgrade -y  
run apt-get -y install wget git gcc patch python-dev make libxml2 python-
libxml2 python-libxslt1 libxslt1-dev python-ldap libldap2-dev libsasl2-dev
libpcre3-dev libz-dev libssl-dev libgnutls-openssl-dev  
run wget -O -
https://launchpad.net/plone/4.3/4.3.4/+download/Plone-4.3.4-UnifiedInstaller.tgz
| tar -C /tmp/ -zxv  
run apt-get -y install bzip2  
run mkdir -p /usr/local/Zeo/  
run useradd plone -d /usr/local/Zeo -s /bin/bash  
run chown -R plone:plone /usr/local/Zeo /tmp/Plone-4.3.4-UnifiedInstaller  
run su plone -c "cd /tmp/Plone-4.3.4-UnifiedInstaller; ./install.sh zeo
--target=/usr/local/Zeo/"  
run su plone -c "git clone https://github.com/gauthierc/confPloneZeo.git
/usr/local/Zeo/confPloneZeo; cp -r /usr/local/Zeo/confPloneZeo/*
/usr/local/Zeo/zeocluster/ "  
run su plone -c "cd /usr/local/Zeo/zeocluster; bin/buildout -c
deployement.cfg"  
expose 5501  
expose 5502  
expose 8888  
cmd su plone -c "/usr/local/Zeo/zeocluster/bin/supervisord -n"  

