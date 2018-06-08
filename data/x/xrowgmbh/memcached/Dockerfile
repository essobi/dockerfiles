# "ported" by Adam Miller <maxamillion@fedoraproject.org> from  
# https://github.com/fedora-cloud/Fedora-Dockerfiles  
#  
# Originally written for Fedora-Dockerfiles by  
# scollier <scollier@redhat.com>  
FROM centos:centos7  
  
MAINTAINER Björn Dieding <bjoern@xrow.de>  
  
ENV container=docker  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
RUN yum -y install memcached telnet; yum clean all  
ADD memcache-top /usr/bin/memcache-top  
  
EXPOSE 11211  
CMD ["memcached", "-u", "daemon"]  

