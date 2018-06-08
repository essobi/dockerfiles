FROM centos:latest  
  
MAINTAINER Leo Gao <aoingl@gmail.com>  
  
# Install basic packages  
RUN yum -y update \  
&& yum install -y epel-release util-linux wget curl xz gzip tar less grep
findutils vim git tree iproute net-tools  
  
# Install ansible  
RUN yum -y install ansible  
  
# Copy files in current directory to guest  
ADD . /opt/servers-lab/  
  
RUN ansible-playbook -e "systemd_enable=false" -i "localhost," -c local
/opt/servers-lab/servers.yml  
  
VOLUME /var/lib/mysql  
  
# Expose 389 & 636 for LDAP  
EXPOSE 389 636 3306  

