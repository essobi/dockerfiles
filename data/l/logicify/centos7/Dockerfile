FROM centos:7  
MAINTAINER Dmitry Berezovsky <dberezovsky@clockedlegal.com>  
  
# Install EPEL repository  
RUN yum -y install epel-release && yum -y update || true  
  
# Install pre-requiste software  
RUN yum -y install yum-utils git tar acl zip unzip wget lftp && \  
yum clean all  
  
# Create user app and grant permissions on /srv folder  
RUN useradd -m -u 1717 app \  
&& chown -R app:app /srv  

