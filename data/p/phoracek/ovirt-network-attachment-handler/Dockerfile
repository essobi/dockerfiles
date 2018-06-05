FROM centos:7  
MAINTAINER Petr Horacek <phoracek@redhat.com>  
  
RUN \  
yum update -y; \  
yum install -y http://resources.ovirt.org/pub/yum-repo/ovirt-release-
master.rpm; \  
yum install -y vdsm dhclient  
ENV SYSTEMD_IGNORE_CHROOT=yes  
  
RUN yum install -y git python-setuptools python-pbr  
COPY ./ ovirt-network-handler/  
RUN \  
cd ovirt-network-handler; \  
python setup.py install  
  
CMD ovirt-network-attachment-start-handler  

