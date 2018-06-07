FROM centos:centos7  
MAINTAINER debari <debari@goga.co.jp>  
RUN rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-
centos-7-0.el7.ngx.noarch.rpm  
RUN yum install -y epel-release  
RUN yum groupinstall -y "Development tools"  
RUN yum install -y nginx python-setuptools nodejs npm  
RUN easy_install pip  
RUN pip install virtualenv supervisor supervisor-stdout  
RUN virtualenv /opt/venv  
  
RUN npm install -g uglify-js clean-css html-minifier  

