FROM centos:centos6.6  
MAINTAINER jeffrey Brite <jeff@c4tech.com>  
  
# Update CentOS  
RUN yum -y update  
  
# Install Centreon Repository  
RUN yum -y install
http://yum.centreon.com/standard/3.0/stable/noarch/RPMS/ces-
release-3.0-1.noarch.rpm  
  
# Install centreon poller  
RUN yum -y install centreon-poller-centreon-engine  
  
# Install ssh  
RUN yum -y install openssh-server  
  
# Install and configure supervisor  
RUN yum -y install python-setuptools  
RUN easy_install supervisor  
  
# Todo better split file  
ADD scripts/supervisord.conf /etc/supervisord.conf  
  
# Expose port HTTP for the service  
EXPOSE 80 22  
CMD ["/usr/bin/supervisord","--configuration=/etc/supervisord.conf"]  

