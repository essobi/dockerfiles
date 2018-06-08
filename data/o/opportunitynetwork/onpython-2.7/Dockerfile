# Ubuntu Trusty Dockerfile  
# Customized python pip installation due to the bugs in Ubuntu  
# pip seems be messed up in Ubuntu Trusty source: \  
# https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1306991 \  
# https://bugs.launchpad.net/ubuntu/trusty/+source/python-pip/+bug/1308714 \  
FROM ubuntu:14.04  
MAINTAINER Rafał bluszcz Zawadzki <rafal@opportunitynetwork.com>  
RUN cd /tmp/ \  
&& echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install python2.7-dev wget -y \  
&& sudo apt-get install libmysqlclient-dev libffi-dev libcairo1.10-cil
libpangocairo-1.0-0 libcairo-perl libxslt1-dev python-dev libfreetype6-dev
libpng-dev pkg-config libmysqlclient-dev uwsgi-plugin-python uwsgi uwsgi-core
-y \  
&& apt-get remove python-pip \  
&& wget https://bootstrap.pypa.io/get-pip.py \  
&& /usr/bin/python2.7 get-pip.py \  
&& apt-get clean \  
&& echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

