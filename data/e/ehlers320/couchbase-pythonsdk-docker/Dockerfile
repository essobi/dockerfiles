From centos:6  
MAINTAINER Tim Ehlers "ehlerst@gmail.com"  
ADD repos/couchbase.repo /etc/yum.repos.d/couchbase.repo  
RUN rpm -ivh https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y wget tar vim python-devel python-pip.noarch scp git gcc
libcouchbase*  
RUN yum clean all  
RUN pip install couchbase  

