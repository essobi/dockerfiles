FROM centos:centos7  
MAINTAINER Mads Konradsen (madskonradsen)  
  
# - Install basic packages (e.g. python-setuptools is required to have
python's easy_install)  
# - Install yum-utils so we have yum-config-manager tool available  
# - Install inotify, needed to automate daemon restarts after config file
changes  
# - Install jq, small library for handling JSON files/api from CLI  
# - Install supervisord (via python's easy_install - as it has the newest 3.x
version)  
RUN \  
yum update -y && \  
yum install -y epel-release && \  
yum install -y iproute python-setuptools hostname inotify-tools yum-utils
which jq && \  
yum clean all && \  
  
easy_install supervisor  
  
# Add supervisord.conf, bootstrap.sh files  
COPY container-files /  
  
ENTRYPOINT ["/config/bootstrap.sh"]  

