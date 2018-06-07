# Setup Memcached on CentOS 6  
# Memcached is part of EPEL Repository  
  
FROM centos  
MAINTAINER Jete O'Keeffe <https://github.com/jeteokeeffe/docker-centos-
memcached>  
# Setup Memcached  
RUN rpm -Uvh http://mirror.metrocast.net/fedora/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum update -y  
RUN yum install -y memcached  
  
# Port to expose *outside* the container  
EXPOSE 11211  
# Service to run  
CMD /usr/bin/memcached -d -p 11211 -u memcached -m 64 -c 1024  

