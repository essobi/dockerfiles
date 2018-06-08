#  
# Description:  
# OpenERP 7.0  
# NextTao  
#  
FROM ubuntu:12.04  
# MAINTAINER Albert "shuaizhe.xu@nexttao.com"  
RUN \  
locale-gen en_US.UTF-8 && \  
locale-gen zh_CN.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
  
# Common  
RUN apt-get update  
RUN \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y build-essential cron curl git htop libxml2 logrotate lsb-
release man sgml-base software-properties-common python-software-properties
ssl-cert sudo unzip vim wget xml-core  
  
# Python 2.7  
RUN \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y python-pip python-dev python2.7-dev build-essential python-
setuptools && \  
easy_install -U distribute  
  
# Other Dependencies  
RUN \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y libpq5 libpq-dev libxml2-dev libxslt1-dev libxslt1.1
libldap2-dev libsasl2-dev swig swig2.0 freetds-dev  
  
RUN apt-get install -y redis-server  
  
# OpenERP v7 still uses PIL, not Pillow  
# http://stackoverflow.com/q/2485295/707580  
# RUN rm -rf /usr/lib/python2.7/site-packages/PIL  
# RUN rm -rf /usr/lib/python2.7/site-packages/PIL.pth  
RUN apt-get install -y libfreetype6 libfreetype6-dev libjpeg-turbo8 libjpeg8
libjpeg-dev libpng12-dev liblcms1 zlib1g-dev  
RUN \  
ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib && \  
ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib && \  
ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib  
RUN apt-get install -y python-imaging  
  
# http://stackoverflow.com/q/18230956/707580  
RUN apt-get install python-tz  
  
# https://github.com/odoo/odoo/blob/8.0/requirements.txt  
# not stable yet  
COPY requirements.txt /  
RUN pip install -r requirements.txt  
  
COPY additional.txt /  
RUN pip install -r additional.txt  
  
# OpenOffice  
RUN sudo add-apt-repository ppa:upubuntu-com/office  
RUN sudo apt-get update  
RUN apt-get install -y openoffice python-uno  
ENV UNO_PATH=/opt/openoffice.org/basis3.4/program  
ENV HOME=/home/openerp  
  
  
RUN rm -rf /var/lib/apt/lists/*  
  
# openerp, the system user  
RUN adduser --system --home=/home/openerp --group openerp  
RUN usermod -s /bin/bash openerp  

