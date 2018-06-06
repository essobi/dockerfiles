# This file describes how to build Plone into a runnable linux container with
all dependencies installed  
# To build:  
# 1) Install docker (http://docker.io)  
# 2) Run:  
# docker run -d <imageid>  
#  
# VERSION 0.1  
# DOCKER-VERSION 0.7.2  
from gauthierc/plone  
MAINTAINER Gauthier C.  
run echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
run apt-get update; apt-get upgrade -y; apt-get -y install aptitude  
run aptitude -y install rubygems  
run aptitude -y -R install ghostscript tesseract-ocr tesseract-ocr-fra pdftk
graphicsmagick poppler-utils poppler-data libreoffice  
run gem install docsplit;cd /usr/bin/;ln -s /usr/local/bin/docsplit  
run sed -i 's/^\\(eggs.*\\)$/\1\n collective.documentviewer/'
/usr/local/Zeo/zeocluster/extend-buildout.cfg  
run su plone -c "cd /usr/local/Zeo/zeocluster; bin/buildout -c
deployement.cfg"  
expose 5501  
expose 5502  
expose 8888  
cmd su plone -c "/usr/local/Zeo/zeocluster/bin/supervisord -n"  

