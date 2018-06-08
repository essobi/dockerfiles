FROM centos:latest  
MAINTAINER Sebastián Magrí <sebasmagri@gmail.com>  
  
# Add repos  
# EPEL  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6Server/x86_64/epel-
release-6-8.noarch.rpm  
# 10gen's MongoDB  
ADD ./files/mongodb.repo /etc/yum.repos.d/mongodb.repo  
  
# Deps  
RUN yum update -y && yum install -y mongodb-org-server gcc python-devel Cython
python-ordereddict python-gunicorn python-gevent supervisor  
  
# Install Marconi 2014.1  
RUN easy_install -U pip setuptools  
RUN pip install
http://tarballs.openstack.org/marconi/marconi-2014.1.tar.gz#egg=marconi
ordereddict  
  
RUN mkdir -p /data/db  
ADD ./files/supervisord.conf /etc/supervisord.conf  
ADD ./files/marconi.conf /etc/marconi/marconi.conf  
  
# Marconi and MongoDB  
EXPOSE 80 27017  
CMD ["/usr/bin/supervisord"]  

