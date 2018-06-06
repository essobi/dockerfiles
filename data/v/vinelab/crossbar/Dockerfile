FROM centos:7  
MAINTAINER Abed Halawi <abed.halawi@vinelab.com>  
  
RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
  
RUN yum install -y libffi-devel python-pip gcc openssl-devel python-devel  
RUN pip install virtualenv  
RUN virtualenv python-venv  
  
WORKDIR /python-venv  
RUN . bin/activate  
  
RUN pip install crossbar[all]  
  
RUN crossbar version  
  
WORKDIR /  
  
CMD crossbar start --cbdir /.crossbar  

