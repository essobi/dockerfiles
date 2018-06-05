#ansible-tower dockerfile  
# WORK IN PROGRESS  
# DO NOT USE IN PRODUCTION  
FROM centos:7  
MAINTAINER tim@arctium.io  
  
ENV TOWER_VER 3.0.3  
# Enable EPEL-Repo, install Ansible  
RUN yum update -y \  
&& yum install -y sudo \  
&& yum install -y http://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& yum install -y ansible  
  
# Download and install Tower  
RUN cd /opt \  
&& curl -O http://releases.ansible.com/ansible-tower/setup/ansible-tower-
setup-${TOWER_VER}.tar.gz \  
&& tar xvzf ansible-tower-setup-${TOWER_VER}.tar.gz \  
&& cd ansible-tower-setup-${TOWER_VER}  
  
ADD inventory /opt/ansible-tower-setup-${TOWER_VER}/inventory  
  
RUN cd /opt/ansible-tower-setup-${TOWER_VER} \  
&& su root \  
&& ./setup.sh  
  
EXPOSE 443 8080  

