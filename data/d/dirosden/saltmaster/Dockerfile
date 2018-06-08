FROM centos:centos7  
  
LABEL name="CentOS Base Image"  
LABEL vendor="CentOS"  
LABEL license=GPLv2  
  
ENV REFRESHED_AT 2016-12-15  
# - Install basic packages (e.g. python-setuptools is required to have
python's easy_install)  
# - Install yum-utils so we have yum-config-manager tool available  
# - Install jq, small library for handling JSON files/api from CLI  
# - Install supervisord (via python's easy_install - as it has the newest 3.x
version)  
RUN yum update -y && \  
yum install -y epel-release && \  
yum install -y iproute python-setuptools hostname yum-utils which jq python-
pip && \  
  
# Salt and prerequisites  
yum install -y salt-master \  
salt-minion \  
salt-ssh \  
virt-what && \  
  
# Additional tools  
yum install -y net-tools nmap git && \  
  
# Clean Up  
yum clean all && \  
  
# Supervisor  
easy_install supervisor && \  
  
# Beacon tols  
easy_install pyinotify dirsync  
  
# Moving Runtime Configuration for Main Components - Supervisor and Salt
Minion  
ADD config /config  
ADD etc /etc  
ADD srv /srv  
  
RUN mkdir -p /var/log/supervisor  
  
# Expose volumes  
VOLUME ["/var/log/supervisor"]  
  
# Expose ports for salt  
EXPOSE 4505  
EXPOSE 4506  
RUN ["chmod", "+x", "/config/bootstrap.sh"]  
RUN ["chmod", "+x", "/config/init/configureenv.sh"]  
RUN ["chmod", "+x", "/config/init/setupminion.sh"]  
  
#Running the Start Script  
CMD ["/config/bootstrap.sh"]  

