FROM centos:centos6  
MAINTAINER saisa6153  
  
USER root  
WORKDIR /root  
  
# yum  
RUN yum install -y http://linux.mirrors.es.net/fedora-
epel/6Server/x86_64/epel-release-6-8.noarch.rpm  
RUN yum update -y  
RUN yum --nogpgcheck install -y passwd sudo gcc gcc-c++ make git openssl-devel
zlib-devel bzip2 bzip2-devel libevent-devel openssh openssh-server readline-
devel tar expat-devel ntp mysql-devel hostname python-pip  
RUN yum install -y http://nginx.org/packages/centos/6/noarch/RPMS/nginx-
release-centos-6-0.el6.ngx.noarch.rpm  
RUN yum install -y --enablerepo=nginx nginx  
RUN yum clean all  
  
# supervisord  
RUN /usr/bin/pip install supervisor  
  
# ruby  
RUN git clone https://github.com/tagomoris/xbuild  
RUN xbuild/ruby-install 2.1.2 /opt/ruby  
  
CMD /bin/bash

